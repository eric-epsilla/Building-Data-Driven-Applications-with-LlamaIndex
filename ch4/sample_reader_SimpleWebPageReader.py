from llama_index.legacy.readers.web import SimpleWebPageReader
from llama_index.legacy.readers.web import BeautifulSoupWebReader
from llama_index.legacy.readers.web import TrafilaturaWebReader


urls = ["https://docs.llamaindex.ai"]
documents = SimpleWebPageReader().load_data(urls)

for doc in documents:
    print(doc.text)
