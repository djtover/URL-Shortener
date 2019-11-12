from flask import Flask, render_template,request
import sqlite3

from sqlite3 import OperationalError
import string
try:
    from urllib.parse import urlparse
    str_encode = str.encode
except Error:
    str_encode = str


host = 'http://localhost:5000/'

# This a method to check if the table has been created
# if it hasn't then it will create the table URLS
def table_check():
    create_table = """
        CREATE TABLE URLS(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        URL TEXT NOT NULL
        );
        """
    with sqlite3.connect('urls.db') as conn:
        cursor = conn.cursor()
        try:
            cursor.execute(create_table)
        except OperationalError:
            pass








app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        original = str_encode(request.form.get('url'))
        if urlparse(original).scheme == '':
            url = 'http://' + original
        else:
            url = original
        with sqlite3.connect('urls.db') as conn:
            cursor = conn.cursor()
            res = cursor.execute(
                'INSERT INTO URLS (URL) VALUES (?)',
                [original]
            )
            index = res.lastrowid
        return render_template('home.html', short_url=host + index)
    return render_template('home.html')

if __name__ == '__main__':
    table_check()
    app.run(debug=True)
