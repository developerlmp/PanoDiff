import os
import csv
import firebase_admin
from firebase_admin import credentials, firestore
from flask import Flask, render_template, jsonify
from pyngrok import ngrok

# Initialize Flask app
app = Flask(__name__)

# Set the Ngrok auth token
ngrok.set_auth_token("2rCwrD8WuljsKpx7ypx03wvnw5q_4sZT1zEPYFLhfWKtckLoH") # CS ID

# Open an HTTP tunnel on the specified port
PORT = 8041
public_url = ngrok.connect(PORT)
print(f" * Ngrok tunnel \"{public_url}\" -> http://127.0.0.1:{PORT}")

# Initialize Firebase Admin SDK
cred = credentials.Certificate("panodiff-42e4a-firebase-adminsdk-6a165-bea7b186a1.json")  # Path to your Firebase service account key
firebase_admin.initialize_app(cred)

# Initialize Firestore client
db = firestore.client()

# Path to CSV file in the current directory
CSV_FILE_PATH = os.path.join(os.getcwd(), "image_labels.csv")

def load_csv_labels():
    """
    Load labels from the CSV file.
    """
    if not os.path.exists(CSV_FILE_PATH):
        print(f"CSV file not found at {CSV_FILE_PATH}")
        return {}

    label_map = {}
    with open(CSV_FILE_PATH, mode="r") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            label_map[row["Filename"]] = row["Label"]
    return label_map

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
        # Load label map from CSV
        label_map = load_csv_labels()

        # Query all documents from the "submissions" collection
        submissions_ref = db.collection('submissions')
        docs = submissions_ref.stream()

        # Prepare leaderboard data
        user_scores = {}
        for doc in docs:
            submission = doc.to_dict()
            user_name = submission.get("user_name", "Unknown")
            file_name = submission.get("file")
            predicted_label = submission.get("real_fake_value")
            original_label = label_map.get(file_name)

            if not user_scores.get(user_name):
                user_scores[user_name] = {"correct": 0, "total": 0}

            if original_label is not None:
                user_scores[user_name]["total"] += 1
                if predicted_label == original_label:
                    user_scores[user_name]["correct"] += 1

        # Calculate leaderboard accuracy
        leaderboard = [
            {
                "user": user,
                "accuracy": round((scores["correct"] / scores["total"]) * 100, 2) if scores["total"] > 0 else 0,
            }
            for user, scores in user_scores.items()
        ]

        leaderboard.sort(key=lambda x: x["accuracy"], reverse=True)
        return jsonify(leaderboard), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=PORT, debug=True, use_reloader=False)
