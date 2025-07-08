```python
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.llms import FakeListLLM  # Mock LLM for demo
from langchain.chains import RetrievalQA

# Initialize embeddings
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Load vector store
vectorstore = Chroma(persist_directory="vector_store/chroma_db", embedding_function=embeddings)

# Initialize retriever
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

# Mock LLM responses (replace with real model in production)
responses = [
    "A customer reported this issue. Please investigate.",
    "This complaint suggests a potential policy violation.",
    "Contact the customer for more details."
]
llm = FakeListLLM(responses=responses)

# Create RAG chain
rag_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
    return_source_documents=True
)

# Example query
query = "billing issues with credit card"
result = rag_chain({"query": query})
print("Response:", result["result"])
print("Source Documents:", [doc.page_content for doc in result["source_documents"]])
```
