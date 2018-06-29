from flask import Blueprint
from flask_restplus import Api
from flask_app.users.route import userapi
from flask_app.auth.route import authapi

api1 = Blueprint('api1', __name__, url_prefix='/api')
api = Api(api1,
          title='My Title',
          version='1.0',
          description='A description'
          )

api.add_namespace(authapi)
api.add_namespace(userapi)