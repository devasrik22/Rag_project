import reflex as rx
from rag_project.components.navbar import navbar

def home():
    return rx.box(
        navbar(),

        rx.center(
            rx.vstack(
                rx.heading("AI Document Knowledge Interface", size="9"),
                rx.text("Upload documents and ask questions using advanced RAG pipelines."),
                rx.link(
                    rx.button("Upload Documents", color_scheme="blue"),
                    href="/upload"
                ),
                spacing="6",
                align="start",
            ),
            height="80vh",
        )
    )