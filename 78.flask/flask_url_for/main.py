from flask import Flask,render_template

# app = Flask(__name__,static_url_path='/public') this is how you change static url path to public
app = Flask(__name__,static_folder='assets') #this is how you change static folder location to assets

@app.route("/")
def hello_world():
    return render_template("index.html")
app.run(debug=True)