# app.py

import os
from flask import Flask, request, redirect, url_for, render_template, send_from_directory
from config import BaseConfig
from werkzeug.utils import secure_filename


app = Flask(__name__)
app.config.from_object(BaseConfig)

ALLOWED_EXTENSIONS = set(['doc', 'docx'])
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if allowed_file(file.filename) is False:
            flash('File format should be %s', ALLOWED_EXTENSIONS)
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # @TODO 
            # process the file here
            # then save it to app.config['PROCESSED_FOLDER']
            file.save(os.path.join(app.config['PROCESSED_FOLDER'], filename))
            return redirect(url_for('processed_file', filename=filename))
    return render_template('index.html')

@app.route('/processed/<filename>')
def processed_file(filename):
    return send_from_directory(app.config['PROCESSED_FOLDER'], filename)

if __name__ == '__main__':
    app.run()
