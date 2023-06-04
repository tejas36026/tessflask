from flask import Flask, request
from flask_cors import CORS
from PIL import Image
import pytesseract

app = Flask(__name__)
CORS(app, origins='https://chat.openai.com')

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return 'No image uploaded', 400

    image = Image.open(request.files['image'].stream)
    print(image)
    text = pytesseract.image_to_string(image)
    print(text)
    return text

if __name__ == '__main__':
    app.run()
