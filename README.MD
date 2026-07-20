## AI Engineering Learning 2:
### Learn the most common real-world AI engineering pattern — grounding LLM answers in your own data.

- [ ] Embeddings and vector similarity (cosine similarity, why chunk size/overlap matters)
- [ ] Pick and learn one vector DB: Chroma (easiest to start), pgvector (if you want to stay in Postgres), or Pinecone
- [ ] Chunking strategies (fixed-size, semantic, recursive) and their tradeoffs
- [ ] Hybrid search (keyword + semantic) and reranking
- [ ] Citation/grounding — tracing an answer back to its source chunk

**Resources:**
- [Anthropic: Contextual Retrieval](https://www.anthropic.com/news/contextual-retrieval)
- [Anthropic Embeddings docs](https://docs.anthropic.com/en/docs/build-with-claude/embeddings)
- [Anthropic Academy — Build a RAG system with MongoDB / LlamaIndex](https://www.anthropic.com/learn/build-with-claude)
- [Chroma docs](https://docs.trychroma.com/)

**About:**
Finished creating my first RAG application that uses Python, ChromaDB for storing and "embedding" PDF data with OpenAI embeddings, and LangChain for the RAG pipeline. 
The application allows users to ask questions about Filipino dishes. 
and it retrieves relevant information from the document to provide exclusive answers based on the Recipes in the PDF, provide ingredients, and cooking instructions.
And added a simple other similar dishes recommendation feature based on the user's query.

TODO: Need to refactor the code to make it user-friendly and add more features like a web interface, and more.

**Architecutre**
![Phase 2 RAG Architecture](docs/phase2_rag_architecture.svg)


