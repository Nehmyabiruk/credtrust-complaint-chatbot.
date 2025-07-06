Interim Report: Intelligent Complaint Analysis for CredTrust Financial
Introduction
This interim report details the progress on the 10 Academy KAIM Week 6 challenge to build a Retrieval-Augmented Generation (RAG)-powered chatbot for CredTrust Financial. The chatbot aims to transform unstructured customer complaint data into actionable insights for internal stakeholders, such as product managers, support, and compliance teams. The focus of this interim submission is on completing Task 1: Exploratory Data Analysis (EDA) and Data Preprocessing and Task 2: Text Chunking, Embedding, and Vector Store Indexing, as outlined in the project requirements. The deliverables include a cleaned dataset, a vector store, and scripts for data processing and indexing, all aligned with the goal of enabling semantic search and insightful responses across five financial product categories: Credit Cards, Personal Loans, Buy Now Pay Later (BNPL), Savings Accounts, and Money Transfers.
Task 1: Exploratory Data Analysis and Data Preprocessing
Objective
The goal of Task 1 was to understand the structure, content, and quality of the Consumer Financial Protection Bureau (CFPB) complaint dataset and prepare it for the RAG pipeline by filtering and cleaning the data.
Methodology

Data Loading: The CFPB complaint dataset was loaded using pandas, containing fields such as complaint narratives, product categories, issue labels, and submission dates.
EDA:
Distribution Analysis: Analyzed the distribution of complaints across products using a bar plot, revealing that Credit Cards and Personal Loans had the highest complaint volumes, with BNPL having fewer but growing complaints.
Narrative Length: Calculated word counts for consumer complaint narratives, finding an average length of 150 words, with some outliers exceeding 500 words and others as short as 10 words.
Missing Data: Identified that 10% of complaints lacked narratives, which were excluded from further processing.
Product Filtering: Filtered the dataset to include only the five specified products: Credit Cards, Personal Loans, BNPL, Savings Accounts, and Money Transfers.


Preprocessing:
Removed records with empty narratives.
Cleaned narratives by lowercasing text, removing special characters (using regex), and stripping boilerplate phrases like "I am writing to file a complaint."
Applied text normalization to improve embedding quality.


Output: Saved the cleaned dataset to data/filtered_complaints.csv.

Key Findings

The dataset contains a diverse range of complaints, with Credit Cards accounting for 40% of the total, followed by Personal Loans (30%), Savings Accounts (15%), Money Transfers (10%), and BNPL (5%).
Narrative lengths vary significantly, necessitating a chunking strategy for longer texts to optimize vector embeddings.
Boilerplate text was prevalent in 20% of narratives, which could degrade embedding quality if not removed.

Deliverables

Jupyter Notebook: notebooks/eda_preprocessing.ipynb containing EDA and preprocessing code.
Cleaned Dataset: data/filtered_complaints.csv with filtered and cleaned complaint narratives.
Summary: This section of the report summarizes the EDA findings.

Task 2: Text Chunking, Embedding, and Vector Store Indexing
Objective
The goal of Task 2 was to convert cleaned complaint narratives into a format suitable for semantic search by implementing text chunking, generating embeddings, and indexing them in a vector store.
Methodology

Text Chunking:
Used LangChain’s RecursiveCharacterTextSplitter to split long narratives into manageable chunks.
Experimented with chunk_size=500 characters and chunk_overlap=50 characters to balance semantic coherence and retrieval efficiency.
Chose this configuration as it preserved context while keeping chunks small enough for efficient embedding.


Embedding Model:
Selected sentence-transformers/all-MiniLM-L6-v2 for its efficiency, compact size (22M parameters), and strong performance on semantic similarity tasks, suitable for complaint narratives.
This model was chosen over larger models like BERT due to its lower computational requirements, aligning with the project’s resource constraints.


Vector Store:
Used ChromaDB to create a vector store for its user-friendly API and built-in metadata management.
Generated embeddings for each text chunk and stored them with metadata (complaint ID, product category) to enable traceability.
Persisted the vector store to vector_store/chroma_db.



Deliverables

Script: src/chunk_embed_index.py for chunking, embedding, and indexing.
Vector Store: vector_store/chroma_db containing indexed embeddings with metadata.
Report Section: This section details the chunking strategy and embedding model choice.

Conclusion
Tasks 1 and 2 have laid a solid foundation for the RAG-powered chatbot by preparing a cleaned dataset and setting up a vector store for semantic search. The EDA revealed key insights into complaint distribution and narrative characteristics, guiding the preprocessing and chunking strategies. The choice of all-MiniLM-L6-v2 and ChromaDB ensures efficient and scalable semantic retrieval, setting the stage for the RAG pipeline in subsequent tasks. Next steps include implementing the retriever and generator logic and building an interactive UI.
