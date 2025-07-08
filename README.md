10 Academy KAIM Week 6: Intelligent Complaint Analysis Chatbot

Project Overview

This repository contains the final submission for the 10 Academy KAIM Week 6 challenge, delivering a Retrieval-Augmented Generation (RAG)-powered chatbot for CredTrust Financial. The chatbot processes CFPB complaint data across Credit Cards, Personal Loans, Buy Now Pay Later (BNPL), Savings Accounts, and Money Transfers, providing actionable insights. Submitted on July 8, 2025, the project covers Task 1: EDA and Preprocessing, Task 2: Text Chunking, Embedding, and Vector Store Indexing, Task 3: RAG Pipeline Implementation, and Task 4: UI Development and Qualitative Evaluation.


Repository Structure

data/:
filtered_complaints.csv: Preprocessed sample dataset.


notebooks/:
eda_preprocessing.ipynb: EDA and preprocessing code.


src/:
chunk_embed_index.py: Text chunking, embedding, and indexing script.
rag_pipeline.py: RAG pipeline implementation.
ui.py: Gradio-based UI code.


vector_store/:
chroma_db/: Placeholder ChromaDB vector store.


docs/:
final_report.md: Final report summarizing all tasks.



Task 1: EDA and Preprocessing

Activities: Loaded sample data, analyzed distribution (Credit Cards 40%, Personal Loans 30%, etc.), cleaned narratives.
Deliverables: notebooks/eda_preprocessing.ipynb, data/filtered_complaints.csv.

Task 2: Text Chunking, Embedding, and Indexing

Activities: Chunked narratives (chunk_size=500, chunk_overlap=50), embedded with all-MiniLM-L6-v2, indexed in ChromaDB.
Deliverables: src/chunk_embed_index.py, vector_store/chroma_db/ (placeholder).

Task 3: RAG Pipeline Implementation

Activities: Built a retriever (top 3 chunks) and mock generator, integrated into a RAG pipeline.
Deliverables: src/rag_pipeline.py.

Task 4: UI Development and Qualitative Evaluation

Activities: Developed a Gradio UI, evaluated with 5 queries (relevance 4.2/5, coherence 4.0/5, usefulness 4.0/5).
Deliverables: src/ui.py, evaluation in docs/final_report.md.

Setup Instructions

Clone the repository: Visit <repository-url> and download the files.
Install dependencies:pip install pandas langchain sentence-transformers chromadb numpy matplotlib seaborn gradio


Run the EDA notebook:jupyter notebook notebooks/eda_preprocessing.ipynb


Run the indexing script:python src/chunk_embed_index.py


Run the RAG pipeline (mock mode):python src/rag_pipeline.py


Launch the UI:python src/ui.py



Limitations

Used sample filtered_complaints.csv and placeholder vector_store/chroma_db/ due to missing CFPB dataset.
Mock generator in Task 3; real model (e.g., LLaMA) recommended.
UI tested locally; requires deployment for production.

Next Steps

Integrate a real language model.
Scale with the full CFPB dataset.
Deploy the UI on a cloud platform.

Contact
For questions, reach out to facilitators: Mahlet, Kerod, Rediet, Rehmet.
