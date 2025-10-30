from flask import Flask,request,jsonify

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def json():
    marks={
        "sarfaraj":67,
        "pratik":46,
        "prathmesh":66,
        "annur":35,
        "vaishnavi":90
    }
    return jsonify(marks)
app.run(debug=True)