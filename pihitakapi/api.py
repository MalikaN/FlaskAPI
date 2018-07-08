from flask import Blueprint,Flask,request
from flask_restful import Resource,Api,reqparse
from pihitakapi.resources import create_user, authenticate_user, get_all_posts, add_posts, get_post, token_refresh, get_all_posts_user_id, edit_post
from flask_cors import CORS
from flask_jwt_extended import jwt_required, jwt_refresh_token_required
from werkzeug.datastructures import FileStorage 

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
parse.add_argument('fileUrl', type=str, help='upload images')
parse.add_argument('postId', type=int, help='Post ID')
parse.add_argument('post', help='Post Description')


class createUser(Resource):
    def post(self):
        try:           
            args = parse.parse_args();
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

class getAllPosts(Resource):
    def get(self):
        try:

            return get_all_posts()        
        
        except Exception as e :
            return {'error': str(e)}

class getPost(Resource):
    def get(self,id):
        try:

            return get_post(id)
        
        except Exception as e :
            return {'error': str(e)}

class addpost(Resource):
    def post(self):
        try:
            args = parse.parse_args();
            return add_posts(args['userid'],args['postTitle'],args['post'],args['fileUrl'])
        
        except Exception as e:
            return {'error': str(e)}

class getAllPostsFromUserID(Resource):
    def post(self):
        try:
            args = parse.parse_args();
            userId = args['userid']
            return get_all_posts_user_id(userId)
        except Exception as e:
            return {'error': str(e)}

class editpost(Resource):
    def post(self):
        try:
            args= parse.parse_args();
            return edit_post(args['postId'],args['postTitle'],args['post'],args['fileUrl'])
        except Exception as e:
            return {'error': str(e)}

class TokenRefresh(Resource):
    @jwt_refresh_token_required
    def get(self):
        return token_refresh()
              
api.add_resource(authenticateUser,'/login')
api.add_resource(createUser,'/signup')
api.add_resource(addpost,'/add-post')
api.add_resource(editpost,'/edit-post')
api.add_resource(getAllPosts,'/')
api.add_resource(getPost,'/post/<int:id>')
api.add_resource(getAllPostsFromUserID,'/my-post')