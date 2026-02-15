from langchain_community.document_loaders import TextLoader

# Load text file
loader = TextLoader('cricket.txt', encoding='utf-8')
docs = loader.load()

print(type(docs))        # list
print(len(docs))         # number of documents
print(type(docs[0]))     # Document object

print("\n---- Page Content ----\n")
print(docs[0].page_content)

print("\n---- Metadata ----\n")
print(docs[0].metadata)
