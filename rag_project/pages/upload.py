import reflex as rx
import os
from rag_project.rag_pipeline import process_pdf


class UploadState(rx.State):
    filename: str = ""
    status: str = ""

    async def handle_upload(self, files: list[rx.UploadFile]):
        if not files:
            self.status = "No file selected ❌"
            return

        file = files[0]
        self.filename = file.name

        os.makedirs("uploaded_files", exist_ok=True)

        path = f"uploaded_files/{file.name}"

        with open(path, "wb") as f:
            content = await file.read()
            f.write(content)

        self.status = "File uploaded successfully ✅"

        # Process PDF
        process_pdf(path)


def upload():
    return rx.box(
        rx.vstack(
            rx.heading("Upload Documents 📄", size="8", color="white"),
            rx.text("Upload your PDFs and start chatting", color="white"),

            # 🔥 IMPORTANT FIX HERE
            rx.upload(
                rx.text("Drag & Drop or Click to Upload", color="white"),
                on_drop=UploadState.handle_upload,
                border="2px dashed white",
                padding="60px",
                width="300px",
                text_align="center"
            ),

            rx.text(UploadState.filename, color="white"),
            rx.text(UploadState.status, color="lightgreen"),

            rx.button(
                "Go Home",
                on_click=rx.redirect("/"),
                bg="gray",
                color="white"
            ),

            spacing="5",
            align="center"
        ),

        display="flex",
        justify_content="center",
        align_items="center",
        height="100vh",
        bg="linear-gradient(to right, #0f2027, #203a43, #2c5364)"
    )