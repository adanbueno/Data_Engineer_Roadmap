from flask import Flask, request
from src import UsersRepo


app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "ola, estou na aplicação setada"

@app.route('/insert', methods=['POST'])
def insert():
    
    
    userRepo = UsersRepo()
    body = request.get_json()
    
    userRepo.insert_user(body["name"])
    
    return 'OK'