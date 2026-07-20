import os
from dotenv import load_dotenv
from pydantic import SecretStr

load_dotenv()

class ModelHelper():
    def __init__(self):
        pass

    @staticmethod
    def openai_embedder():
        from langchain_openai import OpenAIEmbeddings
        langchain_openai_api_key = SecretStr(os.getenv("OA_API_KEY"))

        embedding_llm = OpenAIEmbeddings(
            model="text-embedding-3-small",
            api_key=langchain_openai_api_key
        )
        return embedding_llm

    @staticmethod
    def deepseek_chatter(messages):
        from langchain_deepseek import ChatDeepSeek
        langchain_deepseek_api_key = SecretStr(os.getenv("DS_API_KEY"))

        deepseek_llm = ChatDeepSeek(
            model="deepseek-v4-flash",
            temperature=0,
            max_tokens=4096,
            api_key=langchain_deepseek_api_key
        )

        messages = [
            (
                "user",
                messages
            ),
        ]
        message = deepseek_llm.invoke(messages)

        return message