from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<Person %r>' % self.username

    def serialize(self):
        return {
            "username": self.username,
            "email": self.email
        }

class Todo1(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    todoItem = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return '<Todo %r>' % self.username

    def serialize(self):
        return {
            "todoItem": self.todoItem,
            "id": self.id
        }
