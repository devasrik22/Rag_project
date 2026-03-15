import reflex as rx

def about():
    return rx.center(
        rx.vstack(
            rx.heading("About", size="7"),
            rx.text("This is an AI Document Search system built using RAG."),
            spacing="4",
        ),
        height="80vh",
    )