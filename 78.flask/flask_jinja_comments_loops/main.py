from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    marks={
        "john":45,
        "saurabha":99,
        "mark":45,
        "jeff":67,
        "alexa":90,
        "lily":100
    }
    return render_template("index.html",marks=marks)
app.run(debug=True)