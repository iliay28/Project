from flask import Flask, render_template, request, redirect, url_for, session
import os
import pandas as pd

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("home.html", title="Hello")

@app.route("/tovar")
def key():
    return render_template("tovar.html")

@app.route("/tovar1")
def mey():
    return render_template("tovar1.html")

@app.route("/tovar2")
def ney2():
    return render_template("tovar2.html")

@app.route("/tovar3")
def ney3():
    return render_template("tovar3.html")

@app.route("/tovar4")
def ney4():
    return render_template("tovar4.html")

@app.route("/tovar5")
def ney5():
    return render_template("tovar5.html")

@app.route("/tovar6")
def ney6():
    return render_template("tovar6.html")

@app.route("/tovar7")
def ney7():
    return render_template("tovar7.html")

@app.route("/tovar8")
def ney8():
    return render_template("tovar8.html")

app.secret_key = 'your secret key'

@app.route('/register', methods=['GET', 'POST'])
def register():
    # Output message if something goes wrong...
    msg = ''
    # Check if "username", "password" and "email" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
    elif request.method == 'POST':
        # Form is empty...
        msg = 'Please fill out the form!'
    # Show registration form with message (if any)
    return render_template('index.html', msg=msg)

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Output message if something goes wrong...
    msg = ''
    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        # Check if account exists using MySQL
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = %s AND password = %s', (username, password))
        account = cursor.fetchone()
        # If account exists in accounts table in the database
        if account:
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            session['id'] = account['id']

@app.route('/show', methods=['GET', 'POST'])
def show():
    if request.method == 'POST':
        file_name = request.form.get('file_name')
        file_context = request.form.get('file_context')
        fw = open(f'./files/{file_name}', 'w')
        fw.write(file_context)
        fw.close()

    return render_template('show.html', message=file_name)

@app.route("/otziv")
def otziv():
    files_paths = os.listdir('./files')
    list_files = []
    for file_name in files_paths:
        file_content = open(f'./files/{file_name}', 'r').readlines()
        list_files.append([file_name, file_content])
    return render_template('otziv.html', list_files=list_files)



@app.route("/create")
def create():
    return render_template("create.html")

@app.route("/sogl")
def solid():
    return render_template("sogl.html")

@app.route("/FAQ")
def blog():
    return render_template("blog.html")

@app.route('/file/<name>')
def file_fn(name):
    path = f'./files/{name}'
    file_context = open(path, 'r').read()
    return render_template('file.html', file_name=path, file_context=file_context)