from flask import Flask, render_template , request,redirect,url_for
import sqlite3
import string

app = Flask(__name__)

def init_database():
    connection = sqlite3.connect("url_db.db")
    connection.execute("""
            CREATE TABLE IF NOT EXISTS url(
                       id integer primary key autoincrement,
                       long_url text,
                       short_url text
                       )""")
    connection.close()

init_database()


@app.route("/", methods=["GET","POST"]) 
def home():
    if request.method == 'POST':
        url = request.form.get('url')
        return redirect(url_for('result', url=url))
    return render_template("Home.html")



@app.route("/result")
def result():
    url = request.args.get('url')
    result = url_shortner(url)
    return render_template("result.html", result=result)


def url_shortner(url):
    return url

if __name__ == '__main__':
    app.run(debug=True )