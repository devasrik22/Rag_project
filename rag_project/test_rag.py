from rag_project.components.rag_pipeline import process_document, ask_question
print('starting')
process_document('..\\Books\\romeo-and-juliet_PDF_FolgerShakespeare.pdf')
print('processed')
print(ask_question('Who are the main characters?'))
