from flask import Flask, render_template, request
import cv2
import numpy as np
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    if request.method == 'POST':
        file = request.files['image']
        if file:
            image = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_COLOR)
            # Dummy image processing: get dimensions
            height, width = image.shape[:2]
            result = f"Uploaded image size: {width}x{height}px"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
