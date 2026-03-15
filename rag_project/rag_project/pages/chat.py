import reflex as rx

from rag_project.components.rag_pipeline import ask_question


class ChatState(rx.State):

    question: str = ""
    answer: str = ""

    def set_question(self, value: str):
        self.question = value

    def get_answer(self):

        if self.question == "":
            self.answer = "Please enter a question."
            return

        response = ask_question(self.question)

        self.answer = response


def chat():

    return rx.center(
        rx.vstack(

            rx.heading("Chat with your documents", size="7"),

            rx.input(
                placeholder="Ask something...",
                value=ChatState.question,
                on_change=ChatState.set_question,
                width="400px",
            ),

            rx.button(
                "Ask",
                on_click=ChatState.get_answer
            ),

            rx.text(ChatState.answer),

            spacing="4",
        ),
        height="80vh",
    )