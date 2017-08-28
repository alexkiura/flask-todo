from flask import Flask
from flask_restful import Resource, Api, reqparse


app = Flask(__name__)
api = Api(app)

TODOS  = [
    {'task': 'Read the docs'},
    {'task': 'Attend meeting'}
]

parser = reqparse.RequestParser() 
parser.add_argument('task', required=True, help='A task must be provided')

class Index(Resource):
    def get(self):
        return {'message': 'Welcome to the Api'}

class Todo(Resource):
    def get(self, todo_id):
        return TODOS[int(todo_id)]

    def put(self, todo_id):
        args = parser.parse_args()
        task = {'task': args['task']}
        TODOS[int(todo_id)] = task
        return task

    def delete(self, todo_id):
        TODOS[int(todo_id)] = None
        return '', 204


class TodoList(Resource):
    def get(self):
        return TODOS

    def post(self):
        args = parser.parse_args()
        TODOS.append({'task': args['task']})
        return TODOS[-1], 201

# Register endpoints
api.add_resource(TodoList, '/todos')
api.add_resource(Todo, '/todos/<todo_id>')
api.add_resource(Index, '/')

if __name__ == '__main__':
    app.run(debug=True)
