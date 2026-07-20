from langchain_docling.loader import DoclingLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores.utils import filter_complex_metadata # TODO: Need to replace this package as it is deprecated

class MetaDataProcessor:
    def __init__(self):
        self.docling_loader = DoclingLoader

    @staticmethod
    def pdf_chunker():
        file_path = "recipes/The-Philippine-Cookbook.pdf"

        pdf_loader = DoclingLoader(
            file_path=file_path
        )

        docs = pdf_loader.load()

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=2000,
            chunk_overlap=1000,
            length_function=lambda x: len(x),
            is_separator_regex=True
        )

        chunks = text_splitter.split_documents(docs)
        chunks_clean = filter_complex_metadata(chunks)
        return chunks_clean
