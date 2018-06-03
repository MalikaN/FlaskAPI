from flask import Blueprint
from flask_restful import Resource,Api,reqparse
from surveyapi.resources import create_user, authenticate_user, get_all_items, add_items, get_item, secret_item, token_refresh
from flask_cors import CORS
from flask_jwt_extended import jwt_required, jwt_refresh_token_required
import werkzeug

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

#CORS configuration
CORS(api_bp, origins="*", allow_headers=[
    "Content-Type", "Authorization", "Access-Control-Allow-Credentials"],
    supports_credentials=True, intercept_exceptions=False)

parse = reqparse.RequestParser()
parse.add_argument('firstname',type=str,help='User First Name')
parse.add_argument('lastname',type=str,help='User Last Name')
parse.add_argument('email',type=str,help='Email to create user')
parse.add_argument('password',type=str,help='Password to create user')
parse.add_argument('userid',type=int,help='User Id created post')
parse.add_argument('postTitle',type=str,help='Post Title')
parse.add_argument('post',type=str,help='Post Description')
parse.add_argument('file',type=werkzeug.datastructures.FileStorage, location='files')

class createUser(Resource):
    def post(self):
        try:           
            args = parse.parse_args()
            return create_user(args['firstname'],args['lastname'],args['email'],args['password'])
           
        except Exception as e :
            return {'error':str(e)}

class authenticateUser(Resource):
    def post(self):
        try:
            
            args = parse.parse_args()
            password = args['password']
            return authenticate_user(args['email'],password)

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

class addpost(Resource):
    def post(self):
        try:
            args = parse.parse_args()
            return{'file':args['file']}
            # return add_items(args['userid'],args['postTitle'],args['post'],args['file'])
        
        except Exception as e:
            return {'error': str(e)}

class secretResource(Resource): 
    @jwt_required
    def get(self):
        return secret_item()

class TokenRefresh(Resource):
    @jwt_refresh_token_required
    def get(self):
        return token_refresh()
              

# api.add_resource(root,'/')
api.add_resource(authenticateUser,'/login')
api.add_resource(createUser,'/signup')
api.add_resource(addpost,'/add-post')
api.add_resource(getAllItems,'/')
api.add_resource(getItem,'/getitem/<int:id>')
api.add_resource(TokenRefresh, '/secret')