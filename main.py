from chroma import ChromaHelper
import json
from langchain_chroma import Chroma, vectorstores
from openai.types import vector_store
from pydantic import SecretStr
from langchain_docling.loader import DoclingLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores.utils import filter_complex_metadata # TODO: Need to replace this package as it is deprecated


# TODO: Move chunker and embedder to separate helper. Increase chunk size as it seems to not get the full recipe
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


# chunks_clean = filter_complex_metadata(chunks)


chroma_helper = ChromaHelper()
results = chroma_helper.get_results("How to make afritada?")
first_page = results[0][0].page_content
print(first_page)


