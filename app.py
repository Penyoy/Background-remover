from flask import Flask, render_template, request, send_from_directory
from rembg import remove
from PIL import Image
import os

app = Flask(__name__)
UPLOAD_FOLDER = "static/hasil"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hapus', methods=['POST'])
def hapus_bg():
    if 'file' not in request.files:
        return "Gak ada file yang diupload!"
    file = request.files['file']
    if file.filename == '':
        return "Nama file kosong!"

    # Simpan file sementara
    input_path = os.path.join(UPLOAD_FOLDER, file.filename)
    output_path = os.path.join(UPLOAD_FOLDER, "no_bg_" + file.filename)
    file.save(input_path)

    # Hapus background
    input_image = Image.open(input_path)
    output_image = remove(input_image)
    output_image.save(output_path)

    return render_template('index.html', hasil=output_path)

if __name__ == '__main__':
    app.run(debug=True)