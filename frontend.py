import os

from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

import backend

root_dir = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(root_dir, 'static')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Prep image classification model
model = backend.get_model('resnet50')

@app.route('/', methods=['GET', 'POST'])
def home():
  if model is None:
    flash('No model loaded.')

  # File uploaded
  if request.method == 'POST':
    # Check if the POST request has the file part
    if 'file' not in request.files:
      flash('No file part')
      return redirect(request.url)

    upload = request.files['file']
    # If user does not select a file
    if upload.filename == '':
      flash('No selected file')
      return redirect(request.url)

    if upload:
      filename = secure_filename(upload.filename)
      upload.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
      print('in upload', filename)
      return render_template('index.html', filename=filename)

  return render_template('index.html')

if __name__ == '__main__':
  app.config['SESSION_TYPE'] = 'filesystem'
  app.run(debug=True, host='0.0.0.0', threaded=True)
