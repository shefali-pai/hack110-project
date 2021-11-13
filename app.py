from flask import Flask, render_template, request
from helpers import find_princess, user, link_getter


app: Flask = Flask(__name__)

users: list[user] = []
user_number: int = 0

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/quiz', methods=["GET", "POST"])
def quiz():
    if request.method == "POST":
        global users
        global user_number

        fname: str = request.form['fname']
        lname: str = request.form['lname']
        hobby: str = request.form['hobby']
        color: str = request.form['color']
        print(hobby)
        print(color)

        if fname == '' or lname == '':
            return render_template("quiz.html")

        princess: str = find_princess(hobby, color)
        pic_link: str = link_getter(princess)
        new_user: user = user(user_number, fname, lname, princess)
        users.append(new_user)

        user_number += 1

        return render_template("result.html", princess=princess, pic_link=pic_link)
    return render_template("quiz.html")

@app.route('/all-results')
def all_results():
    return render_template('all-results.html', users=users)

@app.route('/user<usernumber>')
def display_user(usernumber: str):
    return render_template('user.html', user=users[int(usernumber)])

if __name__ == '__main__':
    app.run(debug=True)