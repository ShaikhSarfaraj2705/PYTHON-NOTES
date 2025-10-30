from flask import Flask,request,render_template,flash,url_for,redirect
app = Flask(__name__)
app.secret_key="f9dg90gsdg8h9d"
@app.route("/")
def login():
    return render_template("index.html")

@app.route("/logout")
def logout():
    flash("You have been logged out!","info")
    return redirect(url_for("login"))

app.run(debug=True)