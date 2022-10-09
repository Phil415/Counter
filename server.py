from flask import Flask, render_template, session, redirect, url_for
app=Flask(__name__)
app.secret_key = 'random1234'

@app.route('/')
def home ():
    if 'count' in session:
        session['count'] = session['count'] + 1
    else:
        session['count'] = 1
    # return str(session['count'])
    return render_template("home.html", count=session['count'])

@app.route('/destroy_session')
def destroy_session ():
    session.clear()
    return redirect(url_for('home'))

app.run(debug=True)