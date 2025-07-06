import pandas as pd
from langchain.text_splitter import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
import chromadb

# Load cleaned dataset
df = pd.read_csv('data/filtered_complaints.csv')

# Initialize text splitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50,
    length_function=len
)

# Chunk narratives
chunks = []
metadata = []
for idx, row in df.iterrows():
    narrative = row['Consumer complaint narrative']
    complaint_id = row['Complaint ID']
    product = row['Product']
    split_texts = text_splitter.split_text(narrative)
    for i, chunk in enumerate(split_texts):
        chunks.append(chunk)
        metadata.append({
            'complaint_id': str(complaint_id),
            'product': product,
            'chunk_id': f'{complaint_id}_{i}'
        })

# Initialize embedding model
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

# Generate embeddings
embeddings = model.encode(chunks, show_progress_bar=True)

# Initialize ChromaDB client
client = chromadb.PersistentClient(path='vector_store/chroma_db')

# Create or get collection
collection = client.get_or_create_collection(name='complaints')

# Add embeddings to collection
collection.add(
    embeddings=embeddings,
    documents=chunks,
    metadatas=metadata,
    ids=[meta['chunk_id'] for meta in metadata]
)

print('Vector store created and saved to vector_store/chroma_db')
