from flask import Flask, render_template,flash,session,request,url_for,redirect
from content_management import Content
#from flask.ext.session import Session
from dbconnection import connection
from wtforms import Form, BooleanField,TextField,PasswordField,validators
from passlib.hash import sha256_crypt
from MySQLdb import escape_string as thwart
from functools import wraps
import gc



SESSION_TYPE = 'memcache'

TOPIC_DICT = Content()


app = Flask(__name__)
app.secret_key = 'super secret key'

@app.route('/')
def homepage():
    return render_template('home_page.html')


@app.route('/dashboard/')
def dashboard():

    #flash("test!!")
    return render_template('dashboard.html', TOPIC_DICT=TOPIC_DICT )



@app.errorhandler(404)
def page_not_found(e):
    return render_template("404_error.html")



def login_required(f):
	@wraps(f)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return f(*args, **kwargs)
		else:
			flash("You need to login first")
			return redirect(url_for('login_page'))

	return wrap

@login_required
@app.route("/logout/")

def logout():
	session.clear()
	flash("You have been logged out")
	gc.collect()
	return redirect(url_for('dashboard'))







@app.route('/login/', methods=["GET","POST"])
def login():

    error = ''

    try:
        c, conn = connection()
        if request.method == "POST":

            #request_data = request.form.to_dict(flat=False)
            username = request.form['username']

            data = c.execute("SELECT * FROM users WHERE username=(%s)",(username,))
            data = c.fetchone()[2]

            if sha256_crypt.verify(request.form['password'], data):
                session['logged_in'] = True
                session['username'] = request.form['username']

                flash("You are now logged in")
                return redirect(url_for("dashboard"))

            else:
                error = "Invaild credentials, try again."

        gc.collect()
            

        return render_template("login.html" , error=error )


    except Exception as e:
        #flash(e)
        error = "Invaild credentials, try again."
        return render_template('login.html', error=error )



class RegistrationForm(Form):
    username = TextField('Username', [validators.Length(min=4, max=20)])
    email = TextField('Email Address', [validators.Length(min=6, max=50)])
    password = PasswordField('New Password', [validators.Required(), validators.EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the Terms of Service and Privacy Notice(updated jul 20, 2020)',[validators.Required()])


@app.route('/register/', methods=["GET","POST"])

def register_page():
    try:
        form = RegistrationForm(request.form)

        if request.method == "POST" and form.validate():
            username = form.username.data
            email = form.email.data
            password = sha256_crypt.encrypt((str(form.password.data)))
            c,conn = connection()

            x = c.execute("SELECT * FROM users WHERE username=(%s)",(username,))

            if int(x) > 0:
                flash("That username is already taken, please choose another number")
                return render_template('register.html' , form=form)

            else:
                c.execute("INSERT INTO users (username,password,email,tracking) VALUES (%s,%s,%s,%s)",
                    (thwart(username), thwart(password),thwart(email),thwart("/introduction-to-python-programming/")))
                conn.commit()
                flash("thanks for registering!")
                c.close()
                conn.close()
                gc.collect()

                session['logged_in'] = True
                session['username'] = username

                return redirect(url_for('dashboard'))

        return render_template("register.html", form=form)


    except Exception as e:
        return(str(e))



@app.route('/support/')
def support():
    return render_template('support.html')





if __name__ == '__main__':
    # app.config['SESSION_TYPE'] = 'filesystem'

    # sess.init_app(app)

    app.debug = True
    app.run(port=6500)