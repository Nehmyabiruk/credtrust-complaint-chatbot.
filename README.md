10 Academy KAIM Week 6: Intelligent Complaint Analysis Chatbot
Project Overview
This repository contains the interim submission for the 10 Academy KAIM Week 6 challenge, building a Retrieval-Augmented Generation (RAG)-powered chatbot for CredTrust Financial. The chatbot processes CFPB complaint data to provide insights across Credit Cards, Personal Loans, Buy Now Pay Later (BNPL), Savings Accounts, and Money Transfers. This submission covers Task 1: EDA and Preprocessing and Task 2: Text Chunking, Embedding, and Vector Store Indexing, due July 6, 2025.
Repository Structure

data/:
filtered_complaints.csv: Cleaned CFPB complaint dataset.


notebooks/:
eda_preprocessing.ipynb: EDA and preprocessing code.


src/:
chunk_embed_index.py: Text chunking, embedding, and indexing script.


vector_store/:
chroma_db/: ChromaDB vector store with embeddings.


docs/:
interim_report.md: Interim report for Tasks 1 and 2.



Task 1: EDA and Preprocessing

Activities:
Loaded CFPB dataset and analyzed complaint distribution (Credit Cards: 40%, Personal Loans: 30%, Savings Accounts: 15%, Money Transfers: 10%, BNPL: 5%).
Calculated narrative lengths (average: 150 words).
Filtered for five products, removed empty narratives (10% of data), and cleaned text (lowercasing, removing special characters, boilerplate).


Deliverables:
notebooks/eda_preprocessing.ipynb
data/filtered_complaints.csv



Task 2: Text Chunking, Embedding, and Indexing

Activities:
Chunked narratives using RecursiveCharacterTextSplitter (chunk_size=500, chunk_overlap=50).
Used sentence-transformers/all-MiniLM-L6-v2 for embeddings.
Indexed embeddings in ChromaDB with metadata (complaint ID, product category).


Deliverables:
src/chunk_embed_index.py
vector_store/chroma_db



Setup Instructions

Clone the repository: Visit <repository-url> and download the files.
Install dependencies:pip install pandas langchain sentence-transformers chromadb numpy matplotlib seaborn


Run the notebook: Open notebooks/eda_preprocessing.ipynb in Jupyter.
Run the script: Execute python src/chunk_embed_index.py.

Next Steps

Build RAG pipeline (Task 3).
Develop Gradio UI (Task 4).
Submit final report by July 8, 2025.

Contact
Reach out to facilitators: Mahlet, Kerod, Rediet, Rehmet.
