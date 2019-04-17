from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from src.user import User
from src.weather import get_weather
from src.powerRate import get_powerRate
from src.dbHandler import query_db

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
app.config['SECRET_KEY'] = 'Nero-God-will-get_HD'



@login_manager.user_loader
def load_user(id):
    return get_user(id)


def get_user(email):
    user_form = query_db("SELECT * FROM user WHERE username = ?;",(email,),one=True)
    if user_form is None:
        return None
    else:
        return User(user_form)





@app.route('/')
def index():
    return render_template("login.html")


@app.route('/login', methods=["POST"])
def login():
    user = get_user(request.form["username"])
    if user is not None and user.password == request.form["password"]:
        login_user(user)
        return redirect(url_for("panel"))
    return render_template("login.html", error=True)





@app.route('/register', methods=["POST"])
def register():
    user = User(request.form)
    user.addUser()
    login_user(user)
    return redirect(url_for("panel"))




@login_required
@app.route("/panel")
def panel():
    city = current_user.city
    state = current_user.state
    weather,temperature = get_weather(city,state)
    power_rate = get_powerRate(city,state)
    return render_template("panel.html",weather=weather, temperature=temperature, power_rate=power_rate)


@app.route('/logout', methods=["POST","Get"])
def logout():
    logout_user()
    return redirect(url_for("index"))


if __name__ == '__main__':
    app.run(port=80,host='0.0.0.0')
