from flask import Flask, render_template, request, redirect, url_for, flash, session
from forms import ContactForm, LoginForm
import csv


app = Flask(__name__, static_url_path='/static')
app.secret_key = 'secretkey'

def check_password(username, password):
    with open('data/usernames.csv') as f:
        for user in csv.reader(f):
            if username == user[0] and password == user[1]:
                return True
    return False

@app.route('/')
def index():
    return render_template('home.html')


@app.route('/about')
def about():

    with open('data/aboutme.csv') as f:
        doc_list = list(csv.reader(f))
    return render_template('about.html',
                         doc_list=doc_list)

@app.route('/projects')
def projects():
    return render_template('projects.html')


@app.route('/contact', methods=('GET', 'POST'))
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        with open('data/messages.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([form.username.data, form.email.data, form.messages.data])
        return redirect(url_for('contact1', name = form.username.data))
    return render_template('contact.html', form=form)

@app.route('/contact1/<name>')
def contact1(name):
    return render_template('contact1.html', name=name)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if check_password(form.username.data, form.password.data):
            password = form.password.data
            username = form.username.data
            session['USERNAME'] = form.username.data
            return redirect('/loginpage')
        else:
            flash('You have entered an incorrect username or password')
    return render_template('login.html', form=form)

@app.route('/loginpage')
def loginpage():
    with open('data/messages.csv') as f:
        doc_list = list(csv.reader(f))
        doc_list = list(filter(None, doc_list))
    return render_template('loginpage.html',
                         doc_list=doc_list)
    return render_template('loginpage.html')

@app.route('/sign_out')
def sign_out():
    session.pop("USERNAME")
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
