from flask import Flask, send_from_directory
import os

base_dir = os.path.dirname(os.path.realpath(__file__))

app = Flask(__name__, static_folder=f'../frontend/dist')

@app.route('/')
def serve_vue():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:path>')
def serve_static_files(path):
    return send_from_directory(app.static_folder, path)

if __name__ == '__main__':
    app.run(debug=True)
