from flask import Flask, request, render_template_string

app = Flask(__name__)

USER_DATA = {
    "username": "admin",
    "password": "1234"
}

LOGIN_FORM = """
<!doctype html>
<html>
<head><title>Login</title></head>
<body>
<h2>Logowanie</h2>
<form method="POST">
  Username: <input type="text" name="username"><br><br>
  Password: <input type="password" name="password"><br><br>
  <input type="submit" value="Zaloguj">
</form>
<p>{{ message }}</p>
</body>
</html>
"""
@app.route('/login', methods=['GET', 'POST'])
def login():
    message = ""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == USER_DATA['username'] and password == USER_DATA['password']:
            message = "Zalogowano pomyślnie!"
        else:
            message = "Nieprawidłowy login lub hasło"
    return render_template_string(LOGIN_FORM, message=message)

if __name__ == '__main__':
    app.run(debug=True)