from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length

app = Flask(__name__)
app.config['SECRET_KEY'] = 'abc123'
Bootstrap(app)


class loginForm(FlaskForm):
    """Account management fields for user login"""
    username = StringField('Username',
                            validators = [InputRequired(),
                                            Length(min=4, max=15)])
    password = PasswordField('Password',
                            validators = [InputRequired(),
                                            Length(min=8, max=80)])
    remember = BooleanField('Remember Me')

class registerForm(FlaskForm):
    """Account management fields for user registration"""
    email = StringField('Email', 
                        validators=[InputRequired(),
                                    Email(message = 'Invalid email'),
                                    Length(max=50)])
    username = StringField('Username',
                            validators = [InputRequired(),
                                            Length(min=4, max=15)])
    password = PasswordField('Password',
                            validators = [InputRequired(),
                                            Length(min=8, max=80)])


@app.route('/')
def index():

    return render_template('index.html') 

@app.route('/login', methods=['GET', 'POST'])
def logIn():

    form = loginForm()

    if form.validate_on_submit():
        return '<h1>' + form.username.data + ' ' + form.password.data + '</h1>'

    return render_template('login.html',
                            form=form)

@app.route('/signup', methods=['GET', 'POST'])
def signUp():

    form = registerForm()

    return render_template('signup.html', 
                            form=form)

@app.route('/dashboard')
def dashboard():

    return render_template('dashboard.html')


if __name__ == '__main__':
    app.debug = True
    # app.jinja_env.auto_reload = app.debug

    # connect_to_db(app)

    # DebugToolbarExtension(app)

    app.run(port=5000, host='0.0.0.0')
