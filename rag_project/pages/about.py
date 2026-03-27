import reflex as rx

def about():
    return rx.box(
        rx.center(
            rx.vstack(
                rx.heading("About Page ℹ️", color="white"),
                rx.text("This is an AI Document Search app using RAG.", color="white"),
            )
        ),
        height="100vh",
        bg="linear-gradient(to right, #0f2027, #203a43, #2c5364)"
    )