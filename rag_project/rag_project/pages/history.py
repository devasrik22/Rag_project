

import reflex as rx

def history():
    return rx.center(
        rx.vstack(
            rx.heading("History Page", size="7"),
            rx.text("Previous queries will appear here."),
            spacing="4",
        ),
        height="80vh",
    )