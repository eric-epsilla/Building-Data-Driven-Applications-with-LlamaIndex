import os
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

os.environ["OPENAI_API_KEY"] = "sk-****"

documents = SimpleDirectoryReader('files').load_data()
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()
response = query_engine.query("summarize each document in a few sentences")

print(response)
