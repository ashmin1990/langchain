from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

# Initialize the vector store with the existing DB
vectorstore1 = Chroma(
    persist_directory="langchain-vectorDB/chroma_db",
    embedding_function=OpenAIEmbeddings(),
    collection_name="sample"
)

# meta-data filtering
results1 = vectorstore1.similarity_search(
    query='Who among these are a bowler?',
    k=2)

for i, doc in enumerate(results1):
    print(f"\n--- Result {i+1} ---")
    print(doc.page_content)

# Initialize the vector store with the existing DB
vectorstore2 = Chroma(
    persist_directory="langchain-vectorDB/chroma_db",
    embedding_function=OpenAIEmbeddings(),
    collection_name="my_collection"
)

results2 = vectorstore2.similarity_search("What is Chroma used for?", k=2)

for i, doc in enumerate(results2):
    print(f"\n--- Result {i+1} ---")
    print(doc.page_content)