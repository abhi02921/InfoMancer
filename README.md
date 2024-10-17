# AI Assistant Chat Application

This application is a conversational AI assistant that integrates a Flask backend with a Streamlit frontend. The app allows users to upload documents, query a database using natural language, and receive AI-generated responses based on the input provided. It also features speech recognition capabilities for user input.

## Features

- **Conversational Interface**: Users can interact with the AI assistant via text or voice input.
- **Document Ingestion**: Users can upload various document types (TXT, PDF, MD) for processing.
- **Search Functionality**: Users can query the system to retrieve relevant information from the uploaded documents.
- **Index Management**: The app can fetch collections with storage indices and manage document ingestion.
- **Speech Recognition**: Users can provide input through voice, which is converted to text for processing.

## Technologies Used

- **Backend**: Flask
- **Frontend**: Streamlit
- **Speech Recognition**: SpeechRecognition library
- **Document Processing**: PyPDF2, python-docx
- **Data Management**: langchain, faiss-cpu
- **Environment Management**: python-dotenv

## Installation

### Prerequisites

Make sure you have Python 3.7 or higher installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

### Clone the Repository

````bash
git clone
cd your-repo-name

```Install Dependencies
It is recommended to use a virtual environment. You can set up a virtual environment and install dependencies using:

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt


```Configuration
Create a .env file in the root of your project directory to define the necessary environment variables:

bash
Copy code
SEARCH_API=http://localhost:5004/query
INGEST_API=http://localhost:5004/ingest-files
INDEX_API=http://localhost:5004/get-indexes
Running the Application
Start the Flask Backend

In one terminal window, run the Flask app:

python app.py
This will start the Flask server on http://localhost:5004.

Start the Streamlit Frontend

In another terminal window, run the Streamlit app:

streamlit run streamlit_app.py
This will start the Streamlit server on http://localhost:8501.
````
