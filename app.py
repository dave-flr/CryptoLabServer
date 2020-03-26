from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)


class Encode(Resource):
    @staticmethod
    def get():
        method = request.args.get('method')
        text = request.args.get('text')
        return {'method': method, 'text': text}, 200


class Decode(Resource):
    @staticmethod
    def get():
        method = request.args.get('method')
        text = request.args.get('text')
        return {'method': method, 'text': text}, 200


api.add_resource(Encode, '/encode')
api.add_resource(Decode, '/decode')

if __name__ == '__main__':
    app.run(debug=True)
