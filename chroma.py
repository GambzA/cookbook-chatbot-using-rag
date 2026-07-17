import os
from languagemodels import ModelHelper
from langchain_chroma import Chroma, vectorstores

embedding_llm = ModelHelper.openai_embedder()

class ChromaHelper:
    def __init__(self):
        self.embedding_llm = ModelHelper.openai_embedder()
        self.vectorStore = None

    @staticmethod
    def check_if_db_exists():
        if not os.path.exists("chroma_db"):
            return False
        return True

    def create_chroma_db(self, embeddings):
        if not self.check_if_db_exists():
            Chroma.from_documents(
                documents=embeddings,
                collection_name="cooking_recipes",
                embedding=self.embedding_llm,
                persist_directory="./chroma_db"
            )

    def call_chroma_db(self):
        if self.check_if_db_exists():
            self.vectorStore = Chroma(
                collection_name="cooking_recipes",
                embedding_function=self.embedding_llm,
                persist_directory="./chroma_db"
            )
        return None

    def get_results(self, query):
        if self.check_if_db_exists():
            self.call_chroma_db()
            results = self.vectorStore.similarity_search_with_relevance_scores(query, k=1)
            return results
        return None