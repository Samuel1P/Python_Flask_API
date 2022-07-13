from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Student(Resource):
    def get(self, name):
        return {"message": f"your name is {name}"}
    

api.add_resource(Student, "/name/<string:name>")


app.run(port=8000)