from funcs_auxiliares_desafio_4 import  make_json
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename


UPLOAD_FOLDER = '/api_flask_desafio_4/'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/csv_converter", methods=['POST', 'GET'])
def get_csv():
    return render_template('index.html')


@app.route("/json", methods=['POST', 'GET'])
def show_json():
    if request.method == 'POST':
        file = request.files['myfile']
        file.save(f'./{secure_filename(file.filename)}')
        if file and file.filename.endswith('.csv'):
            return make_json(f'./{secure_filename(file.filename)}')

    return "No file uploaded or wrong file format."
