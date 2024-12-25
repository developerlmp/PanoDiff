import os
import firebase_admin
from firebase_admin import credentials, firestore
from flask import Flask, render_template, jsonify
from pyngrok import ngrok

# Initialize Flask app
app = Flask(__name__)

# Set the Ngrok auth token (ensure you have your token here)
ngrok.set_auth_token("2qOSQBHxYCC2pz0jBRRZQ7DFTpX_2JyS3Rju7VLGYpF9jWmv3")

# Open an HTTP tunnel on the specified port
PORT = 8040
public_url = ngrok.connect(PORT)
print(f" * Ngrok tunnel \"{public_url}\" -> http://127.0.0.1:{PORT}")

# Initialize Firebase Admin SDK
cred = credentials.Certificate("panodiff-42e4a-firebase-adminsdk-6a165-d68006a13b.json")  # Path to your Firebase service account key
firebase_admin.initialize_app(cred)

# Initialize Firestore client
db = firestore.client()

@app.route('/')
def index():
    """
    Render the main dashboard HTML.
    """
    return render_template('index.html')

@app.route('/get-data')
def get_data():
    """
    Fetch data from Firestore and return it as JSON.
    """
    try:
        # Query all documents from the "submissions" collection
        submissions_ref = db.collection('submissions')
        docs = submissions_ref.stream()

        # Convert Firestore documents to a list of dictionaries
        data = []
        for doc in docs:
            submission = doc.to_dict()
            submission['id'] = doc.id  # Include document ID if needed
            data.append(submission)

        return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=PORT, debug=True, use_reloader=False)
