from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Bonjour depuis Flask via Nginx !"

@app.route('/about')
def about():
    return "Ceci est la page À propos."

@app.route('/contact')
def contact():
    return "Ceci est la page Contact."

@app.route('/hello/<name>')
def hello(name):
    return f"Bonjour, {name} !"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
