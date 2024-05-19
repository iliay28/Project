from flask import Flask, render_template, request, redirect
import os
import pandas as pd

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("home.html", title="Hello")

@app.route("/tovar")
def key():
    return render_template("tovar.html")

@app.route("/register")
def registracia():
    return render_template("index.html")

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
    files_paths.remove('deleted_files')
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