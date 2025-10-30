from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def hello_world():

    if "name" in request.args.keys():
        name=request.args['name']
    if "token" in request.args.keys():
        token=request.args['token']
    return render_template("index.html",name=name,token=token)
app.run(debug=True)