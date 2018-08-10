from flask import Flask, render_template, redirect, session, request
import random
app = Flask(__name__)
app.secret_key = "WowSuchSecret"

@app.route('/')
def root():
    if not 'number' in session:
        session['number'] = random.randrange(0, 101)
    print session['number']
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result_post():
    session['guess'] = int(request.form['guess'])
    gameStr = ""
    if session['guess'] > session['number']:
        gameStr += "Too High!"
    if session['guess'] < session['number']:
        gameStr += "Too Low!"
    if session['guess'] == session['number']:
        gameStr += "You win!"
    session['gameStr'] = gameStr
    print type(session['guess'])
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session.clear()
    return redirect('/')

app.run(debug=True)