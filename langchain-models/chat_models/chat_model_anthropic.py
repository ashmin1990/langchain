from langchain_openai import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

chat_model = ChatAnthropic(model="claude-3-5-sonnet-20241022",temperature=1.5,max_completion_tokens=10)
result = chat_model.invoke("Write 1 line statement about Odisha culture")
print(result.content)