from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Простой список для хранения пар пользователей
users = [{'username': 'admin', 'password': 'admin'}]

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        for user in users:
            if user['username'] == username and user['password'] == password:
                return redirect(url_for('birthday'))
        
        return "Неверное имя пользователя или пароль"
    
    return render_template('login.html')

@app.route('/birthday')
def birthday():
    return render_template('birthday.html')

if __name__ == '__main__':
    app.run(debug=True)
