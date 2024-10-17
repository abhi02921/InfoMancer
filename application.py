import os
from flask import Flask, jsonify, request
from routes.document_route import doc_ingestion_route_blueprint

app = Flask(__name__)

# Setup upload folder and allowed file extensions
app.config['UPLOAD_FOLDER'] = './uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'md'}

app.register_blueprint(doc_ingestion_route_blueprint)


@app.route('/')
def home():
    return jsonify(message="Welcome to the Document Ingestion API!"), 200

# Example API endpoint


@app.route('/api/data', methods=['GET'])
def get_data():
    # Dummy data to send to Streamlit
    return jsonify({"data": "This is some data from Flask!"})


if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(port=5004)
