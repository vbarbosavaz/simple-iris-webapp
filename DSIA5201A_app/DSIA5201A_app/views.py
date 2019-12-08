from DSIA5201A_app import app
from flask import Flask, request, render_template

@app.route('/')
def index():
    return render_template('index.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(403)
def forbidden_page(error):
    return render_template("403.html"), 403

@app.errorhandler(500)
def server_error_page(error):
    return render_template("500.html"), 500
