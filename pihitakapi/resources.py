from flask import jsonify
from flaskext.mysql import MySQL
from datetime import datetime, timedelta
from pihitakapi.config import BaseConfig
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, get_jwt_identity, get_raw_jwt,decode_token)
import bcrypt
# import cloudinary
import os
# from cloudinary.uploader import upload
# from cloudinary.utils import cloudinary_url

mysql = MySQL()
upload_url = 'https://api.cloudinary.com/v1_1/myprojectx/image/upload/'
import jwt
# CLOUDINARY = {
#     'cloud_name' : 'myprojectx',
#     'api_key' : '936153933364769',
#     'api_secret' : 'j3sI_Od0qbzbBGNtumI4SbIC5Do'
# }


def create_user(firstname,lastname,email,password):

    conn = mysql.connect()
    cursor = conn.cursor()
    __firstName = firstname
    __lastName = lastname
    __userEmail = email
    __password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    cursor.callproc('spCreateUser',(__firstName,__lastName,__userEmail,__password.decode('utf-8'),))
    data = cursor.fetchone()

    if (data[0]!=[]):
        conn.commit()
        # JWT access
        access_token = create_access_token(identity = email)
        refresh_token = create_refresh_token(identity = email)
        tokenValue = dict()
        tokenValue['message'] = ('logged in as '+email)
        tokenValue['access_token'] = access_token
        tokenValue['refresh_token'] = refresh_token
        tokenValue['userId'] = format(data[0])
        tokenValue['username'] = (firstname+' '+lastname)
        tokenValue['status'] = 422

        return tokenValue
    else:
        return {'status':'100','Message': str(data[0])}


def authenticate_user(email,password):

    conn = mysql.connect()
    cursor = conn.cursor()
    __email = email

    cursor.callproc('spAuthenticateUser',(__email,))
    data = cursor.fetchone()

    if(len(data)>0):
        passwd = str(data[4])
        if bcrypt.checkpw(password.encode('utf-8'), passwd.encode('utf-8')):
            access_token = create_access_token(identity = format(data[0]))
            refresh_token = create_refresh_token(identity = format(data[0]))
            tokenValue = dict()
            tokenValue['message'] = format('logged in as {}'.format(data[3]))
            tokenValue['access_token'] = access_token
            tokenValue['refresh_token'] = refresh_token
            tokenValue['userId'] = format(data[0])
            tokenValue['username'] = format(data[1])+' '+format(data[2])
            tokenValue['status'] = 422
            
            return tokenValue

        else:
            return {'status':100,'message':'Authentication failure'}

def get_all_posts():

    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.callproc('spGetPosts')
    data = cursor.fetchall()
    post_List = []
    
    for post in data:
        i = {
            'id' : post[0],
            'postTitle' : post[1],
            'PostDesc' : post[2],
            'PostSrc' : post[4],
            'CatId': post[5],
            'Slug': post[6],
            'CustomCode': post[7],
            'Category': post[9]
            }
        post_List.append(i)

    return {'StatusCode':'200','Items':post_List}

def get_category():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.callproc('spGetPostCategory')
    data = cursor.fetchall()
    category_List = []

    for cat in data:
        i = {
            'catId' : cat[0],
            'Category' : cat[1]
        }
        category_List.append(i)

    return {'StatusCode':'200','category':category_List}

def get_post(CustomCode):

    __cCode = CustomCode
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.callproc('spGetSinglePost',(__cCode,))
    data = cursor.fetchall()
    singlePost = []
    for post in data:
        i = {
            'postId' : post[0],
            'postTitle' : post[1],
            'PostDesc' : post[2],
            'PostSrc' : post[4],
            'createdUser': post[8]
            }
        singlePost.append(i)
    return {'StatusCode':'200','Items':singlePost}


def add_posts(uId, pTitle, postDesc, selectedFile, catId, slug, cid, accno, mobile, city):

    # fileName = os.path.join(upload_url,selectFile)
    # return {'result':'selectFile'}
    # cloudinary.uploader.unsigned_upload(fileName,'iv3w5ot5',cloud_name = 'myprojectx')
    conn = mysql.connect()
    cursor = conn.cursor()  
    cursor.callproc('spAddPost',(uId, pTitle, postDesc, selectedFile, catId, slug, cid, accno, mobile, city,))   
    data = cursor.fetchall()
    
    if len(data) is 0:
        conn.commit()
        return {'StatusCode':'201','Message': 'Post created Successfully'}
    else:
        return {'StatusCode':'100','Message': 'Error Occured'}

def get_all_posts_user_id(userid):

    conn =mysql.connect()
    cursor = conn.cursor()
    __userID = userid
    cursor.callproc('spGetAllPostFromLoginUser',(__userID,))
    data = cursor.fetchall()
    allPosts = []

    for post in data:
        i={
            'postId' : post[0],
            'postTitle' : post[1],
            'PostDesc' : post[2],
            'PostSrc' : post[4],
            'Slug' : post[6],
            'CustomCode' : post[7]
        }

        allPosts.append(i)
    
    return{'StatusCode':'200','Items':allPosts}

def edit_post(postid, title, post, file):

    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.callproc('spEditPost',(postid, title, post, file))
    data = cursor.fetchall()

    if len(data) is 0:
        conn.commit()
        return {'StatusCode':'201','Message': 'Post created Successfully'}
    else:
        return {'StatusCode':'100','Message': 'Error Occured'}

def token_refresh():
    current_user = get_jwt_identity()
    access_token = create_access_token(identity = current_user)
    return {'access_token': access_token}  