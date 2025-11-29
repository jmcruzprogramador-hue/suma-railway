#!/usr/bin/env python3
from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__, static_folder='static', static_url_path='')

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/suma', methods=['POST'])
def suma():
    # Intentar JSON
    if request.is_json:
        data = request.get_json()
        a = data.get('a', 0)
        b = data.get('b', 0)
    else:
        # Formulario clásico
        a = request.form.get('a', 0)
        b = request.form.get('b', 0)

    try:
        a = float(a)
        b = float(b)
        resultado = 'PEPE'#a * b
        return jsonify({'resultado': resultado})
    except (ValueError, TypeError):
        return jsonify({'error': 'Los parámetros a y b deben ser numéricos'}), 400


if __name__ == '__main__':
    # En local puedes usar el puerto 5000, Railway pondrá el suyo con env var
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
