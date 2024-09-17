from flask import Flask, request, jsonify
from constants import class_pred, get_class_name
import keras
from werkzeug.utils import secure_filename
from flask_cors import CORS
import os

# Load the model
model = keras.saving.load_model("../model.h5")

app = Flask(__name__)
CORS(app)

# Configure upload folder
UPLOAD_FOLDER = './files'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['ALLOWED_EXTENSIONS'] = {'wav', 'mp3', 'aac', 'flac'}
app.config['MAX_CONTENT_LENGTH'] = 100 * 1000 * 1000

# Ensure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/predict', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 401
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 402
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        
        response = get_class_name(class_pred(model, file_path))
        return jsonify({'class': response}), 200
    
    return jsonify({'error': 'File type not allowed'}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8989)
