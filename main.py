from flask import Flask, render_template
import sqlite3
from sqlite3 import Error




# This a method to check if the table has been created
# if it hasn't then it will create the table URLS
def table_check():
    create_table = """
        CREATE TABLE URLS(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        URL TEXT NOT NULL
        );
        """
    with sqlite3.connect('url.db') as conn:
        cursor = conn.cursor()
        try:
            cursor.execute(create_table)
        except Error:
            pass




app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    table_check()
    app.run(debug=True)
