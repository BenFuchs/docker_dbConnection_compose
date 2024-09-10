from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password@mysql:3306/mydatabase'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Optional: Disable tracking modifications to save resources

db = SQLAlchemy(app)

# Define a User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

@app.route('/')
def index():
    db.create_all()
    # Fetch all users from the database
    users = User.query.all()
    
    # Format the result as a list of dictionaries
    users_list = [{"id": user.id, "name": user.name} for user in users]
    
    # Return JSON response
    return jsonify(users=users_list)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
