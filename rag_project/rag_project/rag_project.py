import reflex as rx

from rag_project.pages.home import home
from rag_project.pages.upload import upload
from rag_project.pages.chat import chat
from rag_project.pages.history import history
from rag_project.pages.about import about


app = rx.App()

app.add_page(home, route="/")
app.add_page(upload, route="/upload")
app.add_page(chat, route="/chat")
app.add_page(history, route="/history")
app.add_page(about, route="/about")