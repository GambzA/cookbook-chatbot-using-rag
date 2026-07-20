import metadataprocessor
from chroma import ChromaHelper
from metadataprocessor import MetaDataProcessor
from languagemodels import ModelHelper
from langchain_core.prompts import ChatPromptTemplate


processor = MetaDataProcessor()
chroma_helper = ChromaHelper()

# processed_data = processor.pdf_chunker()
# chroma_helper.create_chroma_db(processed_data)

prompt_template = """
    You are a recipe search engine and you are provided with the context below:
    {context}

    Answer questions that are related to the user's search query: {query}

    Follow this format below:

    1. Title
    2. Ingredients
    3. Steps (follow a proper step format, or enhance current step for better understanding)
    4. Estimate completion time, and difficulty to make
    5. Provide other recipes with relevant main ingredients
"""

query = "What is the recipe for Steamed White Chicken?"

results = chroma_helper.get_results(query)

context_text = "\n\n---\n\n".join([document.page_content for document, _score in results])
chat_object_initialize = ChatPromptTemplate.from_template(prompt_template)
prompt = chat_object_initialize.format(context=context_text, query=query)

print(ModelHelper.deepseek_chatter(prompt).content)