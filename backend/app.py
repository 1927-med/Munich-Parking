from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
from flask_bcrypt import Bcrypt
from flask_mail import Mail
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
app.config['MAIL_SERVER'] = 'your-mail-server'
app.config['MAIL_PORT'] = 'your-mail-port'
app.config['MAIL_USERNAME'] = 'your-mail-username'
app.config['MAIL_PASSWORD'] = 'your-mail-password'

db = sqlite3.connect('database.db')
bcrypt = Bcrypt(app)
mail = Mail(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    user_data = cursor.fetchone()
    if user_data:
        user = User(user_data[1], user_data[2])
        user.id = user_data[0]
        return user
    return None

class User(UserMixin):
    def __init__(self, username, password):
        self.id = None
        self.username = username
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def save_to_db(self):
        cursor = db.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (self.username, self.password))
        db.commit()

    def get_id(self):
        return self.id

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Register')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        cursor = db.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (form.username.data,))
        user_data = cursor.fetchone()
        if user_data and bcrypt.check_password_hash(user_data[2], form.password.data):
            user = User(user_data[1], user_data[2])
            user.id = user_data[0]
            login_user(user)
            return redirect(url_for('dashboard'))
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(form.username.data, form.password.data)
        user.save_to_db()
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)