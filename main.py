from flask import Flask
from flask import render_template, request, redirect, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sekretnyklucz'

@app.route('/mypage/me')
def aboutme():
    return render_template("me.html")

@app.route('/mypage/contact')
def contact():
    return render_template("contact.html")

@app.route('/mypage/contact', methods=['GET', 'POST'])
def message():
    if request.method == 'POST':
        message = request.form.get("message")
        flash('Twoja wiadomość {} została wysłana!'.format(message))
        return redirect('/mypage/contact')
    
