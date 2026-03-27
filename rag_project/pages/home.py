import reflex as rx

def home():
    return rx.box(

        # 🔷 NAVBAR
        rx.hstack(
            rx.hstack(
                rx.text("🧠", font_size="24px"),
                rx.text("AI Document Search", font_weight="bold", font_size="18px"),
            ),

            rx.spacer(),

            rx.hstack(
                rx.link("Home", href="/"),
                rx.link("Upload Document", href="/upload"),
                rx.link("Chat", href="/chat"),
                rx.link("History", href="/history"),
                rx.link("About", href="/about"),
                spacing="4",
            ),

            padding="15px",
            bg="#2c2f7f",
            color="white"
        ),

        # 🔷 HERO SECTION
        rx.hstack(

            # LEFT TEXT
            rx.vstack(
                rx.heading(
                    "Chat with Your Documents using AI",
                    size="9",
                    color="white"
                ),

                rx.text(
                    "Upload PDFs or text files and ask questions. "
                    "Our AI uses Retrieval-Augmented Generation (RAG) "
                    "to give accurate, source-based answers.",
                    color="white",
                    font_size="16px"
                ),

                rx.button(
                    "Get Started",
                    bg="blue",
                    color="white",
                    margin_top="10px"
                ),

                align_items="start",
                spacing="4",
                width="50%"
            ),

            # RIGHT IMAGE
            rx.image(
                src="/brain.png",
                width="350px"
            ),

            padding="60px",
        ),

        # 🔷 BACKGROUND COLOR
        height="100vh",
        background="linear-gradient(90deg, #0f2027, #203a43, #2c5364)"
    )