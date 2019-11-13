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
        return render_template('home.html', short_url=host + str(index))
    return render_template('home.html')

# def getId(short_url):
#     i = short_url.find(':5000')
#     i = i + 6
#     for j in short_url
#         if(short_url[j]< 0 or short_url[j] > 9)
#             raise ValueError('Invalid URL')
#     ans = int(short_url[i:])
#     return ans


@app.route('/<short_url>')
def redirect_url(short_url):
    # try:
    #     id = getId(short_url);
    #     pass
    # except Exception as e:
    #     raise
    id = short_url
    url = localhost
    with sqlite3.connect('urls.db') as connect:
        cursor = connect.cursor()
        result = cursor.execute('SELECT URL FROM URLS WHERE ID=?', id)
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
