from langchain_docling.loader import DoclingLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores.utils import filter_complex_metadata # TODO: Need to replace this package as it is deprecated

class MetaDataProcessor:
    def __init__(self):
        self.docling_loader = DoclingLoader

    @staticmethod
    def pdf_chunker():
        # TODO: need to change chunking strategy, will try parent-child retrieval
        file_path = "recipes/pinoy-recipes.pdf"

        pdf_loader = DoclingLoader(
            file_path=file_path
        )
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=50,
            length_function=lambda x: len(x),
            is_separator_regex=True
        )

        chunks = text_splitter.split_documents(pdf_loader.load())
        chunks_clean = filter_complex_metadata(chunks)
        return chunks_clean
