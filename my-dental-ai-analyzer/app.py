from flask import Flask, render_template, request, send_from_directory
import os
import cv2
import numpy as np

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
RESULT_FOLDER = 'static/results'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['RESULT_FOLDER'] = RESULT_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def upload_file():
    if 'image' not in request.files:
        return 'No file part', 400
    file = request.files['image']
    if file.filename == '':
        return 'No selected file', 400

    if file:
        filename = file.filename
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # Process the image (just an example - replace with your tooth analysis logic)
        img = cv2.imread(filepath)
        result_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Dummy step, replace with actual analysis

        # Save the result
        result_filepath = os.path.join(app.config['RESULT_FOLDER'], 'result.jpg')
        cv2.imwrite(result_filepath, result_img)

        return render_template('index.html', result="Teeth Analysis Complete!", result_image='results/result.jpg')

if __name__ == "__main__":
    app.run(debug=True)
