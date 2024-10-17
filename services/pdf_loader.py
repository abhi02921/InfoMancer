import os
import tempfile
from PyPDF2 import PdfReader
from langchain.docstore.document import Document
import logging

logger = logging.getLogger(__name__)


class PDFLoader:
    def __init__(self, folder_path):
        self.folder_path = folder_path

    def load(self):
        docs = []
        for filename in os.listdir(self.folder_path):
            if filename.endswith(".pdf"):
                file_path = os.path.join(self.folder_path, filename)
                docs.extend(self.load_pdf(file_path))
        return docs

    def load_pdf(self, file_path):
        with open(file_path, 'rb') as file:
            reader = PdfReader(file)
            text = ''
            for page in reader.pages:
                text += page.extract_text()
            return [Document(page_content=text, metadata={"source": file_path})]

    def load_pdfs_from_request(self, files):
        documents = []

        for file in files:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
                temp_file.write(file.read())
                temp_file.seek(0)

                reader = PdfReader(temp_file.name)
                pdf_content = ""
                for page in reader.pages:
                    pdf_content += page.extract_text()

                logger.debug(pdf_content, "--")
                documents.append(
                    Document(page_content=pdf_content, metadata={"source": file.filename}))

        return documents
