from flask import Flask,request,render_template

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def hello_world():
    # print(request.method) 
    # print(request.form) 
    if request.method == "POST":
        print(request.form)
        name = request.form["name"]
        print(name)
    return render_template("contact.html")
app.run(debug=True)