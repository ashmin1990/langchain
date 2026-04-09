from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

chat_model = ChatOpenAI(model="gpt-4",temperature=1.5,max_completion_tokens=10)
result = chat_model.invoke("Write 1 line statement about Indian culture")
print(result.content)