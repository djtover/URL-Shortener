
from flask import Flask, render_template,request,redirect
import sqlite3
from sqlite3 import OperationalError
import string
try:
    from urllib.parse import urlparse
    str_encode = str.encode
except Error:
    str_encode = str



host = 'http://localhost/'

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
# This is a method that if it is a POST protocol then insert that URL into the DB and return the new shortened URL
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        original = str_encode(request.form.get('url'))
        with sqlite3.connect('urls.db') as conn:
            cursor = conn.cursor()
            res = cursor.execute(
            'INSERT INTO URLS (URL) VALUES (?)',
            [original]
            )
            index = res.lastrowid
            return render_template('home.html', short_url=host + str(index))
    return render_template('home.html')



# This is a method that when a shortened URL is inputed then get the URL from
# the DB based on the ID the URL has and redirect the shortened URL to the long one
@app.route('/<short_url>')
def redirect_url(short_url):
    id = short_url
    url = host
    with sqlite3.connect('urls.db') as connect:
        cursor = connect.cursor()
        res = cursor.execute('SELECT URL FROM URLS WHERE ID=?', [id])
        try:
            short = res.fetchone()
            if short is not None:
                url = short[0]
        except Exception as e:
            print(e)
    return redirect(url)

if __name__ == '__main__':
    table_check()
    app.run(debug=True)
