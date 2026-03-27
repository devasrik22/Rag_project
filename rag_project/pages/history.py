import reflex as rx

def history():
    return rx.box(
        rx.center(
            rx.vstack(
                rx.heading("History Page 📜", color="white"),
                rx.text("No history yet...", color="white"),
            )
        ),
        height="100vh",
        bg="linear-gradient(to right, #0f2027, #203a43, #2c5364)"
    )