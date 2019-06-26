"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from models import db, Person, Todo1

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)

@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

@app.route('/')
def sitemap():
    return generate_sitemap(app)



@app.route('/todolist', methods=['POST', 'GET'])
def handle_todo():
    """
    Create person and retrieve all persons
    """

    # POST request
    if request.method == 'POST':
        body = request.get_json()

        if body is None:
            raise APIException("You need to specify the request body as a json object", status_code=400)
        if 'todoItem' not in body:
            raise APIException('You need to specify the item', status_code=400)


        todo11 = Todo1(todoItem=body['todoItem'])
        db.session.add(todo11)
        db.session.commit()
        return "ok", 200

    # GET request
    if request.method == 'GET':
        all_doing = Todo1.query.all()
        all_doing = list(map(lambda x: x.serialize(), all_doing))
        return jsonify(all_doing), 200

    return "Invalid Method", 404

@app.route('/todolist/<int:todo_id>', methods=['PUT', 'GET', 'DELETE'])
def get_single_todo(todo_id):
    """
    Single person
    """

    # PUT request
    if request.method == 'PUT':
        body = request.get_json()
        if body is None:
            raise APIException("You need to specify the request body as a json object", status_code=400)

        todo11 = Todo1.query.get(todo_id)
        if todo11 is None:
            raise APIException('User not found', status_code=404)

        if "todoItem" in body:
            todo11.todoItem = body["todoItem"]
        db.session.commit()

        return jsonify(todo11.serialize()), 200

    # GET request
    if request.method == 'GET':
        todo11 = Todo1.query.get(todo_id)
        if todo11 is None:
            raise APIException('User not found', status_code=404)
        return jsonify(todo11.serialize()), 200

    # DELETE request
    if request.method == 'DELETE':
        todo11 = Todo1.query.get(todo_id)
        if todo11 is None:
            raise APIException('User not found', status_code=404)
        db.session.delete(todo11)
        db.session.commit()
        return "ok", 200
        # if request.method == 'DELETE':
        # user1 = Person.query.get(person_id)
        # if user1 is None:
        #     raise APIException('User not found', status_code=404)
        # db.session.delete(user1)
        # db.session.commit()
        # return "ok", 200

    return "Invalid Method", 404


if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT)