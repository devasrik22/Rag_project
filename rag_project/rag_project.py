import reflex as rx
class State(rx.State):
    chat_history: list[tuple[str, str]] = []

    def add_message(self, question, answer):
        self.chat_history.append((question, answer))

    def clear_chat(self):
        self.chat_history = []

# ------------------ NAVBAR ------------------ #
def navbar():
    return rx.hstack(
        rx.text("🧠 AI Document Search", font_size="24px", font_weight="bold"),
        rx.spacer(),

        rx.menu.root(
            rx.menu.trigger(
                rx.button("☰ Menu", bg="#3b82f6", color="white")
            ),
            rx.menu.content(
                rx.menu.item("Home", on_click=rx.redirect("/")),
                rx.menu.item("Upload", on_click=rx.redirect("/upload")),
                rx.menu.item("Chat", on_click=rx.redirect("/chat")),
                rx.menu.item("History", on_click=rx.redirect("/history")),
                rx.menu.item("About", on_click=rx.redirect("/about")),
            )
        ),

        padding="15px",
        bg="#2d2f7f",
        color="white"
    )

# ------------------ FOOTER ------------------ #
def footer():
    return rx.box(
        rx.hstack(
            # LEFT
            rx.vstack(
                rx.heading("AI Document Search", size="5"),
                rx.text("Ask questions from your documents using AI-powered RAG."),
                rx.text("© 2026 AI Document Search. All rights reserved.", font_size="12px"),
                spacing="2",
                align="start"
            ),

            # CENTER
            rx.vstack(
                rx.heading("Quick Links", size="5"),
                rx.link("Home", href="/"),
                rx.link("Upload", href="/upload"),
                rx.link("Chat", href="/chat"),
                rx.link("History", href="/history"),
                spacing="2",
                align="start"
            ),

            # RIGHT (🔥 ICONS ADDED HERE)
            rx.vstack(
                rx.heading("Connect", size="5"),

                rx.link(
                    rx.hstack(
                        rx.icon("github", size=20),
                        rx.text("GitHub"),
                    ),
                    href="https://github.com/devasrik22",
                    is_external=True,
                    color="white",
                    _hover={"color": "#3b82f6"}
                ),

                rx.link(
                    rx.hstack(
                        rx.icon("linkedin", size=20),
                        rx.text("LinkedIn"),
                    ),
                    href="https://www.linkedin.com/in/devasri-k-90669928a/",
                    is_external=True,
                    color="white",
                    _hover={"color": "#3b82f6"}
                ),

                rx.link(
                    rx.hstack(
                        rx.icon("mail", size=20),
                        rx.text("Email"),
                    ),
                    href="mailto:devasridkk@gmail.com",
                    color="white",
                    _hover={"color": "#3b82f6"}
                ),

                spacing="3",
                align="start"
            ),

            justify="between",
            align="start",
            padding="40px",
            max_width="1200px",
            margin="0 auto"
        ),

        bg="#0a0a0a",
        color="white"
    )

# ------------------ HOME PAGE ------------------ #
def index():
    return rx.flex(

        # 🔹 MAIN CONTENT
        rx.box(
            navbar(),

            rx.hstack(
                rx.vstack(
                    rx.heading(
                        "Chat with Your Documents using AI",
                        size="9",
                        color="white"
                    ),
                    rx.text(
                        "Upload PDFs or text files and ask questions.",
                        font_size="18px",
                        color="white"
                    ),
                    rx.button(
                        "Get Started",
                        bg="#3b82f6",
                        color="white",
                        on_click=rx.redirect("/upload")
                    ),
                    spacing="5",
                    align="start"
                ),

                rx.image(
                    src="/brain.png",
                    width="400px",
                    border_radius="20px"
                ),

                justify="between",
                align="center",
                padding="60px"
            ),

            # 🔥 CHAT HISTORY SECTION
            rx.vstack(
                #rx.heading("Chat History", color="white"),

                rx.foreach(
                    State.chat_history,
                    lambda chat: rx.box(
                        rx.text(f"Q: {chat[0]}", color="white"),
                        rx.text(f"A: {chat[1]}", color="white"),
                        padding="10px",
                        border="1px solid white",
                        border_radius="10px",
                        margin="5px"
                    )
                ),

              

                padding="20px"
            ),

            bg="linear-gradient(to right, #0f2027, #203a43, #2c5364)",
            width="100%",
            flex_grow="1"
        ),

        # 🔹 FOOTER
        footer(),

        direction="column",
        min_height="100vh",
        justify="between"
    )
# ------------------ IMPORT PAGES ------------------ #
from rag_project.pages.home import home
from rag_project.pages.upload import upload
from rag_project.pages.chat import chat
from rag_project.pages.history import history
from rag_project.pages.about import about

# ------------------ APP ------------------ #
app = rx.App()

app.add_page(index, route="/")
app.add_page(upload, route="/upload")
app.add_page(chat, route="/chat")
app.add_page(history, route="/history")
app.add_page(about, route="/about")

