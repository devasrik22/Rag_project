from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

# Load all PDFs inside data folder
loader = DirectoryLoader(
    path="data",
    glob="*.pdf",
    loader_cls=PyPDFLoader
)

documents = loader.load()

print("Total documents loaded:", len(documents))
print("\nFirst document content:\n")
print(documents[0].page_content)
print("\nMetadata:\n")
print(documents[0].metadata)
