from flask import Flask, render_template
import sqlite3
from sqlite3 import Error







app = Flask(__name__)
# host = 'http://localhost:'
@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
