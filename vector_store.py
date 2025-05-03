from langchain.vectorstores import Chroma
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document
import os

CHROMA_DIR = "chroma_db"

embedding = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

def get_vectorstore():
    if os.path.exists(CHROMA_DIR):
        return Chroma(persist_directory=CHROMA_DIR, embedding_function=embedding)
    return None

def save_to_vectorstore(texts, metadata_list=None):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    chunks = text_splitter.create_documents(texts, metadatas=metadata_list or [{}]*len(texts))
    vectordb = Chroma.from_documents(documents=chunks, embedding=embedding, persist_directory=CHROMA_DIR)
    vectordb.persist()
    return vectordb

def query_vectorstore(query, top_k=3):
    vectordb = get_vectorstore()
    if not vectordb:
        return ""
    docs = vectordb.similarity_search(query, k=top_k)
    return "\n".join([doc.page_content for doc in docs])

def save_query_answer(query, answer):
    # Это можно хранить тоже как документ
    doc = Document(page_content=f"Q: {query}\nA: {answer}")
    vectordb = get_vectorstore()
    if vectordb:
        vectordb.add_documents([doc])
        vectordb.persist()

