from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

# Простой список для хранения пар пользователей
users = [{"username": "Fedorov", "password": "admin"}]


@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        for user in users:
            if user["username"] == username and user["password"] == password:
                return redirect(url_for("birthday"))

        return "Неверное имя пользователя или пароль"

    return render_template("login.html", dark_theme=False)


@app.route("/toggle-theme", methods=["POST"])
def toggle_theme():
    dark_theme = request.json.get("dark_theme", False)
    return jsonify(success=True, dark_theme=dark_theme)


@app.route("/birthday")
def birthday():
    return render_template("birthday.html")


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=5000)
