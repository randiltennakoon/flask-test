from flask import Flask, render_template, redirect, url_for, flash

app = Flask(__name__)

app.config['SECRET_KEY'] = 'e8e79d0003846b082d5d1fa03c47ffa2'


@app.route('/')
def home():
    flash("You're in home page", 'success')
    return render_template('home.html', title='Home')


if __name__ == '__main__':
    app.run(debug=True)