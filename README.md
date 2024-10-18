# python vue application example

This is example of python Flask app serving Vue frontend.

## Directory Structure

```
projectRoot/
    +-- frontend/
        +-- dist/
            +-- index.html
        +-- src/
            +-- main.ts
        +-- vite.config.ts
    +-- backend/
        +-- app.py
```

## Vue frontend setup

```sh
mkdir my-app
cd my-app
npx create-vite frontend
cd frontend
yarn && yarn build
```

## Python backend setup

```sh
cd ..
mkdir backend
cd backend
```

Create Python virtual environment:

```sh
python -m venv .venv
source .venv/Scripts/activate
```

Install Flask:

```sh
python -m pip install flask
```

### backend/app.py:

```py
from flask import Flask, send_from_directory
import os

app = Flask(__name__, static_folder=f'../frontend/dist')

@app.route('/')
def serve_vue():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:path>')
def serve_static_files(path):
    return send_from_directory(app.static_folder, path)

if __name__ == '__main__':
    app.run(debug=True)
```

## Running Web app

```sh
uvicorn src.main:app --reload --host 0.0.0.0 --port 5000
```

**WARNING**: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
