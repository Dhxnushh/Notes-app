from flask import Flask,render_template,redirect,session
from cs50 import SQL
app = Flask(__name__)

@app.route("/")
def login():
    return render_template("login.html")


@app.route("/register",methods=["POST","GET"])
def register():
    if method == "POST":
        username = request.form.get('usernam')
        password = request.form.get('passwor')
        cpw = request.form.get('cpassword')
        if cpw!=password:
            return render_template("/register",error='Passwords dont match.')
        

if __name__ == "__main__":
    app.run(debug=True) 