from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('dance.pdf')
docs = loader.load()

print(len(docs))

print("\n--- First Page Content ---\n")
print(docs[0].page_content)

print("\n--- Metadata ---\n")
print(docs[0].metadata)

