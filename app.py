from flask import Flask, request, render_template, send_file
from pdf2docx import Converter
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_convert():
    if request.method == 'POST':
        file = request.files['file']
        if file.filename.endswith('.pdf'):
            file.save('uploaded.pdf')
            docx_file = 'converted.docx'
            Converter('uploaded.pdf').convert(docx_file, start=0, end=None)
            return send_file(docx_file, as_attachment=True)
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)
