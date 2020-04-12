from flask import Flask
from flask_restplus import Resource, Api

app = Flask(__name__)
api = Api(app)

class Serve(Resource):
    def get(self):
        return {'server': 'server-started ...'}

api.add_resource(Serve, '/server')

if __name__ == '__main__':
    app.run(debug=True)