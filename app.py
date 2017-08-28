from flask import Flask
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)


class Index(Resource):
    def get(self):
        return {'message': 'Welcome to the Api'}


api.add_resource(Index, '/')

if __name__ == '__main__':
    app.run(debug=True)
