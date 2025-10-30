from flask import Flask, render_template
from config import config
from models import db
from api.routes import api_bp


app = Flask(__name__)
app.config.from_object(config)


# init DB
db.init_app(app)


# register blueprint
app.register_blueprint(api_bp, url_prefix='/api')


@app.route('/')
def index():
return render_template('index.html')


if __name__ == '__main__':
app.run(debug=True)