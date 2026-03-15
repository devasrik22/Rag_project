import reflex as rx
import os
import shutil

from rag_project.components.rag_pipeline import process_document

UPLOAD_FOLDER = "uploaded_files"


class UploadState(rx.State):

    message: str = ""

    async def handle_upload(self, files: list[rx.UploadFile]):

        if not os.path.exists(UPLOAD_FOLDER):
            os.makedirs(UPLOAD_FOLDER)

        for file in files:

            file_path = os.path.join(UPLOAD_FOLDER, file.filename)

            # remove existing file
            if os.path.exists(file_path):
                try:
                    os.remove(file_path)
                except PermissionError:
                    self.message = "Close the file and try again."
                    return

            with open(file_path, "wb") as buffer:
                shutil.copyfileobj(file.file, buffer)

            process_document(file_path)

        self.message = "File uploaded and processed successfully!"


def upload():

    return rx.center(
        rx.vstack(

            rx.heading("Upload PDF Document", size="7"),

            rx.upload(
                rx.text("Drag and drop PDF here or click to select"),
                on_drop=UploadState.handle_upload,
                multiple=False
            ),

            rx.text(UploadState.message),

            spacing="4"
        ),
        height="80vh"
    )