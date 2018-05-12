from flask import Blueprint
from flask_restful import Resource,Api,reqparse
from surveyapi.resources import create_user, get_all_items, authenticate_user, add_items, get_item
from flask_cors import CORS

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

#CORS configuration
CORS(api_bp, origins="*", allow_headers=[
    "Content-Type", "Authorization", "Access-Control-Allow-Credentials"],
    supports_credentials=True, intercept_exceptions=False)

parse = reqparse.RequestParser()
parse.add_argument('email',type=str,help='Email to create user')
parse.add_argument('password',type=str,help='Password to create user')
parse.add_argument('itemname',type=str,help='Item Name')
parse.add_argument('itemprice',type=float,help='Item price')
parse.add_argument('itemqty',type=int,help='Item Qty')

class root(Resource):
    def get(self):
        return 'hello world'

class createUser(Resource):
    def post(self):
        try:

            args = parse.parse_args()
            return create_user(args['email'],args['password'])
           
        except Exception as e :
            return {'error':str(e)}

class authenticateUser(Resource):
    def post(self):
        try:
            
            args = parse.parse_args()
            return authenticate_user(args['email'],args['password'])
            
        except Exception as e:
            return {'error': str(e)}

class getAllItems(Resource):
    def get(self):
        try:

            return get_all_items()        
        
        except Exception as e :
            return {'error': str(e)}

class getItem(Resource):
    def get(self,id):
        try:

            return get_item(id)
        
        except Exception as e :
            return {'error': str(e)}

class addItems(Resource):
    def post(self):
        try:

            args = parse.parse_args()
            return add_items(args['itemname'],args['itemprice'],args['itemqty'])
        
        except Exception as e:
            return {'error': str(e)}

api.add_resource(root,'/')
api.add_resource(authenticateUser,'/login')
api.add_resource(createUser,'/createuser')
api.add_resource(addItems,'/additems')
api.add_resource(getAllItems,'/getallitems')
api.add_resource(getItem,'/getitem/<int:id>')