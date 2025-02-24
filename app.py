from flask import Flask, render_template, request, jsonify
from transformations import upload_s3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=["POST"])
def upload():
    if "file" not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files["file"]
    filename = file.filename

    file_url = upload_s3(file, filename)

    return jsonify({"message": "File uploaded successfully", "url": file_url})



if __name__ == '__main__':
    app.run(debug=True)