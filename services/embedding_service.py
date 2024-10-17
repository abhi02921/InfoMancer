from langchain.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from utils.env_config import PERSIST_DIRECTORY
from langchain.docstore.document import Document


def create_embeddings(documents, index_name):
    # Split documents into smaller chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, chunk_overlap=150)
    texts = text_splitter.split_documents(documents)

    # Initialize HuggingFaceEmbeddings for the SentenceTransformer model
    embedder = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2")

    # Define the persistence directory in a writable path
    persist_directory = PERSIST_DIRECTORY

    # Create embeddings using the HuggingFaceEmbeddings model and store in ChromaDB
    vectordb = Chroma.from_documents(
        documents=texts,
        embedding=embedder,
        persist_directory=persist_directory,
        collection_name=index_name
    )

    # Persist the vector database
    vectordb.persist()
    vectordb = None
