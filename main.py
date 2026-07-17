import metadataprocessor
from chroma import ChromaHelper
from metadataprocessor import MetaDataProcessor

processor = MetaDataProcessor()
chroma_helper = ChromaHelper()

processed_data = processor.pdf_chunker()
chroma_helper.create_chroma_db(processed_data)


results = chroma_helper.get_results("Chicken recipes")

print (results)

# show all results page contents
for i, (document, score) in enumerate(results):
    print(f"Result {i + 1}:")
    print(f"Page Content: {document.page_content}")
    print(f"Relevance Score: {score}")
    print()