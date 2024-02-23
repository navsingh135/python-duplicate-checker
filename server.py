from flask import Flask
from flask import request
from flask import render_template
from csv_service import findDuplicateRows
from tempfile import TemporaryFile
import os

app = Flask(__name__)

@app.route("/")
def hello_world():
   return render_template('index.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        tempfile = TemporaryFile()
        f.save(tempfile)
        duplictes = findDuplicateRows(tempfile)
        html = ""
        if not duplictes:
            html += '<body<h1>No duplicates found</h1>'
        else:
            html += '<body><h1>Duplicates found</h1>'
            for duplicate in duplictes:
                html += f'<p>{duplicate}</p>'
        html += '</body>'
        return html
    return 'method not allowed'
