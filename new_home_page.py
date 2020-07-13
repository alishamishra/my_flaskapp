from flask import Flask, render_template, flash , session
from content_management import Content
#from flask.ext.session import Session

SESSION_TYPE = 'memcache'

TOPIC_DICT = Content()


app = Flask(__name__)
app.secret_key = 'super secret key'

@app.route('/')
def homepage():
    return render_template('home_page.html')


@app.route('/dashboard/')
def dashboard():

    flash("test!!")
    return render_template('dashboard.html', TOPIC_DICT=TOPIC_DICT )



@app.errorhandler(404)
def page_not_found(e):
    return render_template("404_error.html")



@app.route('/login/')
def login():
    return render_template('login.html')


if __name__ == '__main__':
    # app.config['SESSION_TYPE'] = 'filesystem'

    # sess.init_app(app)

    app.debug = True
    app.run()