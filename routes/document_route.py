import logging
from flask import request, jsonify, Blueprint, abort
from services.pdf_loader import PDFLoader
from repositories.document_repository import DocumentRepository
from services.embedding_service import create_embeddings

logger = logging.getLogger(__name__)

# Blueprint for routes
doc_ingestion_route_blueprint = Blueprint(
    'doc_ingestion_route_blueprint', __name__)
is_pdf_stored_locally = False


@doc_ingestion_route_blueprint.route('/ingest-files', methods=['POST'])
def ingest_documents():
    index_name = request.form.get('index_name', 'default_index')
    uploaded_files = request.files.getlist('files')

    if len(uploaded_files) == 0:
        abort(400, "No files provided to ingest")

    if is_pdf_stored_locally:
        pdf_folder_path = "/Users/abhishek/Documents/gpt-voice-assistant/gpt-voice-assistant/pdfs"

        pdf_loader = PDFLoader(pdf_folder_path)
        pdf_documents = pdf_loader.load()
    else:
        pdf_loader = PDFLoader(folder_path="")
        pdf_documents = pdf_loader.load_pdfs_from_request(uploaded_files)

    logger.debug("PDF data is extracted into text format")

    # Create embeddings and persist
    create_embeddings(pdf_documents, index_name)

    return jsonify({"message": "Documents ingested successfully!"}), 200


@doc_ingestion_route_blueprint.route('/query', methods=['POST'])
def query_documents():
    index_name = request.form.get('index_name', 'default_index')
    query = request.form.get('q')

    if not query:
        abort(400, "Query is not provided")

    logger.debug(f"Query: {query} is asked on index: {index_name}")

    # Call the service to get results
    results = create_embeddings(query, index_name)

    return jsonify({"query": query, "results": results}), 200


@doc_ingestion_route_blueprint.route('/get-indexes', methods=['GET'])
def get_indexes():
    try:
        collection_repository = DocumentRepository()
        documents = collection_repository.get_collection_names_with_storage_index()
        return jsonify(documents), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
