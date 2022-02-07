from distutils.log import error
from flask_restful import Api, Resource, abort, fields
from models.posts import Post,user_posts
from flask import jsonify
import json
import requests

class postRequests(Resource):
    tag_error = {"error":"tag parameter is required"}
    sort_error = {"error":"sortBy paremeter is invalid"}
    dir_error = {"error":"direction parameter is invalid"}

    def __init__(self,tag):
        self.tag = tag
        pass

    def sortId(self,e):
        return e['id']
    def sortReads(self,e):
        return e['reads']
    def sortLikes(self,e):
        return e['likes']
    def sortPop(self,e):
        return e['popularity']

    def deserialize(self,myInput):
        schema = user_posts(many=True)
        result = schema.load(myInput)
        #posts = []
        #for p in myPost["posts"]:
        #    result = schema.load(p)
        #    posts.append(result)
        return result

    def get(self,tag:str,sortBy:str = None,direction:str = None):
        if( not tag):
            tag = self.tag
        if(tag):
            get_data = requests.get('https://api.hatchways.io/assessment/blog/posts',params={"tag":tag})
            result = get_data.json()
            if(sortBy):
                if(sortBy == "id"):
                    if(direction == "desc"):
                        result["posts"].sort(key=self.sortId,reverse=True)
                    elif(direction == "asc" or direction ==None):
                        result["posts"].sort(key=self.sortId)
                    else:
                        return self.dir_error,400
                elif(sortBy == "reads"):
                    if(direction == "desc"):
                        result["posts"].sort(key=self.sortReads,reverse=True)
                    elif(direction == "asc" or direction ==None):
                        result["posts"].sort(key=self.sortReads)
                    else:
                        return self.dir_error,400
                elif(sortBy == "likes"):
                    if(direction == "desc"):
                        result["posts"].sort(key=self.sortLikes,reverse=True)
                    elif(direction == "asc" or direction ==None):
                        result["posts"].sort(key=self.sortLikes)
                elif(sortBy == "popularity"):
                    if(direction == "desc" ):
                        result["posts"].sort(key=self.sortPop,reverse=True)
                    elif(direction == "asc" or direction ==None):
                        result["posts"].sort(key=self.sortPop)
                else:
                    return self.sort_error,400
        else:
           return self.tag_error,400

        return 200