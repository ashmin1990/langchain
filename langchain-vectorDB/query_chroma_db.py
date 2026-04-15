from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

# Initialize the vector store with the existing DB
vectorstore = Chroma(
    persist_directory="langchain-vectorDB/chroma_db",
    embedding_function=OpenAIEmbeddings(),
    collection_name="sample"
)

# meta-data filtering
results = vectorstore.similarity_search_with_score(
    query="",
    filter={"team": "Chennai Super Kings"}
)

print(results)