import os
from flask import Flask, render_template, jsonify, request
from pyngrok import ngrok

# Initialize Flask app
app = Flask(__name__)

# Set the Ngrok auth token (ensure you have your token here)
ngrok.set_auth_token("2qOSQBHxYCC2pz0jBRRZQ7DFTpX_2JyS3Rju7VLGYpF9jWmv3")

# Open an HTTP tunnel on the specified port
PORT = 8040
public_url = ngrok.connect(PORT)
print(f" * Ngrok tunnel \"{public_url}\" -> http://127.0.0.1:{PORT}")

# Function to get all folder names in the static directory
def get_folders():
    static_dir = app.static_folder  # Get path to the static folder
    return [f for f in os.listdir(static_dir) if os.path.isdir(os.path.join(static_dir, f))]

# Route to display the homepage with a dropdown and images
@app.route('/')
def index():
    folders = get_folders()  # Get all folders in the static directory
    return render_template('index.html', folders=folders)


@app.route('/get-images')
def get_images():
    folder = request.args.get('folder')
    image_dir = os.path.join('static', folder)
    images = [f"/static/{folder}/{img}" for img in os.listdir(image_dir)]
    return jsonify(images)



# Run the app
if __name__ == '__main__':
    app.run(port=PORT, debug=True, use_reloader=False)


