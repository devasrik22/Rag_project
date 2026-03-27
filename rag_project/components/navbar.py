import reflex as rx

def navbar():
    return rx.hstack(
        rx.hstack(
            rx.text("🧠", font_size="22px"),
            rx.text(
                "AI Document Search",
                font_weight="bold",
                font_size="20px",
            ),
        ),

        rx.spacer(),

        rx.hstack(
            rx.link("Home", href="/"),
            rx.link("Upload", href="/upload"),
            rx.link("Chat", href="/chat"),
            rx.link("History", href="/history"),
            rx.link("About", href="/about"),
            spacing="5",
        ),

        padding="15px",
        border_bottom="1px solid #444",
        width="100%",
    )
    