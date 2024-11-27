from flask import Flask, request, render_template, redirect, url_for, flash


app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/service')
def services():
    return render_template('service.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/banglow')
def banglow():
    return render_template('banglow.html')

@app.route('/house')
def house():
    return render_template('home.html')

@app.route('/apartment')
def apartment():
    return render_template('apartment.html')


if __name__ == '__main__':
    app.run(debug=True)
