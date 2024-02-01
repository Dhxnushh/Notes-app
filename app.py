from flask import Flask,render_template,redirect,session,request
from cs50 import SQL
app = Flask(__name__)
db = SQL("sqlite:///user.db")
app.config["SECRET_KEY"] = 'notes'

@app.route("/", methods=["POST","GET"])
def login():
    session.clear()
    if request.method =='POST':
        username = request.form.get('usernam')
        password = request.form.get('passwor')
        rows = db.execute('select * from users where name = ?',username)
        if len(rows)!=1:
            return render_template("/",error="Username does not exist")
        if rows[0]['hash']!=password:
            return render_template("/",error="Password is incorrect")
        else:
            session['un']=rows[0]['name']
            session['id']=rows[0]['id']
            return redirect('/home')
    return render_template("login.html")


@app.route("/register",methods=["POST","GET"])
def register():
    if request.method == "POST":
        username = request.form.get('usernam')
        password = request.form.get('passwor')
        cpw = request.form.get('cpassword')
        if cpw!=password:
            return render_template("register.html",error='Passwords dont match.')
        rows = db.execute('select * from users where name = ?',username)
        if len(rows)!=0:
            return render_template("register.html",error = "Username already exists")
        else:
            db.execute('insert into users(name,hash) values(?,?)',username,password)
            rows1 = db.execute('select * from users where name = ?',username)
            db.execute('insert into notes(id,notes) values(?,?)',rows1[0]['id'],"")
            return redirect("/")
    return render_template("register.html")


@app.route("/home",methods=["POST","GET"])
def home():
    if  len(session)==0:
        return redirect("/")
    return render_template("layout2.html")


@app.route("/logout")
def logout():
    return redirect("/")
        

if __name__ == "__main__":
    app.run(debug=True) 