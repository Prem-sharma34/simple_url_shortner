from flask import Flask, render_template , request,redirect,url_for, flash
import sqlite3
import string
import random

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
    long_url = url
    short_url = generate_url()
    address = "http://127.0.0.1:5000/"
    result= address+short_url
    connection = sqlite3.connect('url_db.db')
    cursor = connection.cursor()
    if connection.execute("select short_url from url where short_url = (?)", (short_url,)) == short_url: 
        short_url=generate_url()

    cursor.execute("insert into url (long_url,short_url) values (?,?)",(long_url,short_url))
    connection.commit()
    connection.close()
    return result

def generate_url():
    
    k = 5
    character = string.ascii_letters + string.digits
    random_string = "".join(random.choices(character,k=5))
    return random_string


@app.route("/<short_url>")
def rediret(short_url):
    print(short_url)
    connection = sqlite3.connect("url_db.db")
    connection.row_factory = sqlite3.Row  # So we can access by column name

    cursor = connection.execute("SELECT long_url FROM url WHERE short_url = ?", (short_url,))
    result = cursor.fetchone()

    if result:
        long_url = result["long_url"] 
        return redirect(long_url)
    else:
        return "URL not found", 404


if __name__ == '__main__':
    app.run(debug=True )