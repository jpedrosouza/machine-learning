from flask import Flask, render_template, request
from werkzeug.utils import secure_filename, send_file
import face_detector

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f"../tmp/{secure_filename(f.filename)}")

        face_detector.detect_faces(f"../tmp/{secure_filename(f.filename)}")

        return send_file('../tmp/detect_faces.jpg', as_attachment=True, environ=request.environ)
    else:
        return 'GET'


if __name__ == '__main__':
    app.run(debug=True)
