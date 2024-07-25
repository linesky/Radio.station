from flask import Flask, render_template, send_from_directory
import os
#pip install Flask

app = Flask(__name__)

# Diretório onde os arquivos multimédia estão armazenados
FILES_DIR = 'files'

@app.route('/')
def index():
    # Lista todos os arquivos no diretório FILES_DIR
    files = os.listdir(FILES_DIR)
    return render_template('index.html', files=files)

@app.route('/files/<filename>')
def download_file(filename):
    # Envia o arquivo solicitado ao usuário
    return send_from_directory(FILES_DIR, filename, as_attachment=True)
print("\x1bc\x1b[47;34m")
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

