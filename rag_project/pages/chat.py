import reflex as rx
from rag_project.rag_pipeline import ask_question


class ChatState(rx.State):
    # ✅ Store as tuple (question, answer)
    messages: list[tuple[str, str]] = []
    input_text: str = ""

    def send_message(self):
        if self.input_text:
            question = self.input_text

            # Get AI response
            answer = ask_question(question)

            # ✅ Store correctly as tuple
            self.messages.append((question, answer))

            self.input_text = ""

    def clear_chat(self):
        self.messages = []


def chat():   # ⚠️ THIS NAME IS IMPORTANT
    return rx.box(
        rx.vstack(
            rx.heading("Chat Page 💬", color="white"),

            # ✅ Chat display
            rx.box(
                rx.foreach(
                    ChatState.messages,
                    lambda msg: rx.box(
                        rx.text(f"You: {msg[0]}", font_weight="bold", color="cyan"),
                        rx.text(
                            f"AI: {msg[1]}",
                            color="white",
                            white_space="pre-wrap"   # ✅ IMPORTANT FIX
                        ),
                        padding="10px",
                        border="1px solid white",
                        border_radius="10px",
                        margin="5px"
                    )
                ),
                height="300px",
                overflow="auto",
                border="1px solid white",
                width="100%"
            ),

            rx.input(
                value=ChatState.input_text,
                on_change=ChatState.set_input_text,
                placeholder="Ask something...",
                width="100%"
            ),

            rx.hstack(
                rx.button(
                    "Send",
                    on_click=ChatState.send_message,
                    bg="#3b82f6",
                    color="white"
                ),
                rx.button(
                    "Clear",
                    on_click=ChatState.clear_chat,
                    bg="red",
                    color="white"
                )
            ),

            spacing="4",
            width="400px"
        ),

        display="flex",
        justify_content="center",
        align_items="center",
        height="100vh",
        bg="linear-gradient(to right, #0f2027, #203a43, #2c5364)"
    )