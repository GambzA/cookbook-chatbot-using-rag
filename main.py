import os
from dotenv import load_dotenv
from langchain_chroma import Chroma, vectorstores
from langchain_deepseek import ChatDeepSeek
from langchain_openai import OpenAIEmbeddings
from openai.types import vector_store
from pydantic import SecretStr
from langchain_docling.loader import DoclingLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores.utils import filter_complex_metadata # TODO: Need to replace this package as it is deprecated

load_dotenv()

langchain_deepseek_api_key = SecretStr(os.getenv("DS_API_KEY"))
langchain_openai_api_key = SecretStr(os.getenv("OA_API_KEY"))

# FILE_PATH = "pinoy-recipes.pdf"
#
# pdfLoader = DoclingLoader(
#     file_path=FILE_PATH
# )
# text_splitter = RecursiveCharacterTextSplitter(
#     chunk_size=1000,
#     chunk_overlap=500,
#     length_function=lambda x: len(x),
#     is_separator_regex=False
# )
#
# chunks = text_splitter.split_documents(pdfLoader.load())

embedding_llm = OpenAIEmbeddings(
    model="text-embedding-3-small",
    api_key=langchain_openai_api_key
)

# chunks_clean = filter_complex_metadata(chunks)

# vector_storage = Chroma.from_documents(
#     # documents=chunks_clean,
#     collection_name="cooking_recipes",
#     embedding=embedding_llm,
#     persist_directory="./chroma_db"
# )

vector_storage = Chroma(
    collection_name="cooking_recipes",
    embedding_function=embedding_llm,
    persist_directory="./chroma_db"
)

test_query = "Please give a recipe for Afritada"

results = vector_storage.similarity_search_with_relevance_scores(test_query, k=3)

print(results)


# deepseek_llm = ChatDeepSeek(
#     model="deepseek-v4-flash",
#     temperature=0,
#     max_tokens=4096,
#     api_key=langchain_deepseek_api_key
# )
#

#



# for chunk in chunks:
#     documents.append(chunk.page_content)
#     ids.append(id)
#     metadata.append(chunk.metadata)
#
#     id += 1

# vector_storage.upsert_documents(documents)


# def get_file_content(file_path):
#     with open(file_path, 'r') as file:
#         return file.read()
#
# def export_analysis_to_file(analysis, output_file):
#     if analysis["stop_reason"] == "max_tokens":
#         print("Warning: response was truncated because max_tokens was reached.")
#
#     with open(output_file, 'w') as file:
#         file.write(analysis)


# messages = [
#     (
#         "system",
#         "You are a code analyst responsible for analyzing code and providing insights. " \
#         "You will receive code snippets and your task is to analyze them and provide a detailed report on their functionality, potential issues, and suggestions for improvement. " \
#         "Your analysis should be thorough and cover all aspects of the code, including logic, structure, readability, and performance." \
#         "Do not provide thinking steps or reasoning, only provide the final analysis report.",
#     ),
#     (
#         "user",
#         get_file_content("demo.html")
#     ),
# ]
# message = deepseek_llm.invoke(messages)
#
#
# print(message.content)
# export_analysis_to_file(message.content, "analysis_output.md")


