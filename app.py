from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:kxpth4fRVHpHJabGAHYp@database-test-1.ckn5btyj4l8v.eu-north-1.rds.amazonaws.com:5432/postgres'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

# pw : kxpth4fRVHpHJabGAHYp

@app.route('/')
def index():
    return jsonify(test="hej")

@app.route('/post', methods=['POST'])
def post():
    name = request.json.get("name", None)
    if name:
        user = User(name = name)
        db.session.add(user)
        db.session.commit()
    else:
        return 'bad request!', 500