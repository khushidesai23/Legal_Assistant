import os
from flask import Flask, render_template, request, session, redirect, url_for
from flask_babel import Babel, get_locale, gettext
from flask_session import Session

app = Flask(__name__)
babel = Babel(app)

app.config['SESSION_TYPE'] = 'filesystem'
app.secret_key = os.environ.get('FLASK_SECRET_KEY')


app.config['BABEL_DEBUG'] = True
# Initialize Flask-Session with the 'app' instance, not named 'Session'
Session(app)

# Configure supported languages
app.config['LANGUAGES'] = {
    'en': 'English',
    'hi': 'Hindi',
}

# Language selector route
@app.route('/setlang/<lang>')
def set_language(lang):
    session['lang'] = lang
    print(f"Session lang set to: {session['lang']}")  # Add this line for debugging
    return redirect(request.referrer)

# Define a custom locale selector function
def custom_locale_selector():
    if 'lang' in session:
        return session['lang']
    return request.accept_languages.best_match(app.config['LANGUAGES'].keys())

# Initialize Flask-Babel using babel.init_app
babel.init_app(app, locale_selector=custom_locale_selector)

# Index route

@app.route('/')
def home():
    current_lang = session.get('lang', 'Default')
    return render_template('file1.html', current_lang=current_lang)
@app.route('/kyr')
def ask_query():
    current_lang = session.get('lang', 'Default')
    return render_template('kyr.html', current_lang=current_lang)
@app.route('/labour')
def labour():
    current_lang = session.get('lang', 'Default')
    return render_template('labour.html', current_lang=current_lang)


if __name__ == '__main__':
    app.run(debug=True)
