from flask_restful import Resource
from models.posts import user_posts
from flask import jsonify,json
import json
import requests
import asyncio

class postRequests(Resource):
    def __init__(self):
        self.tag_error = {"error":"tag parameter is required"}
        self.sort_error = {"error":"sortBy paremeter is invalid"}
        self.dir_error = {"error":"direction parameter is invalid"}
        self.tag_store = []
        self.cache_storage = {}

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
        return json(result)

    def serialize(self,input_posts):    
        mySchema = user_posts(many=True)
        j_result = mySchema.dump(input_posts)
        return j_result

    def cache_store(self,tag):
        if(tag in self.tag_store):
            print("brought from cache")
            return self.cache_storage[tag]
        else:
            print("stored to cache")
            self.tag_store.append(tag)
            get_data = requests.get('https://api.hatchways.io/assessment/blog/posts',params={"tag":tag})
            json_data = get_data.json()
            self.cache_storage[tag] = json_data
            return json_data

    def get(self,tag:str,sortBy:str = None,direction:str = None):
        if(tag):
            #get_data = requests.get('https://api.hatchways.io/assessment/blog/posts',params={"tag":tag})
            get_data = self.cache_store(tag)
            #result = get_data.json()
            result = get_data
            if(sortBy):
                if(sortBy == "id"):
                    if(direction == "desc"):
                        result["posts"].sort(key=self.sortId,reverse=True)
                    elif(direction == "asc" or direction == None):
                        result["posts"].sort(key=self.sortId)
                    else:
                        return jsonify(self.dir_error),400
                elif(sortBy == "reads"):
                    if(direction == "desc"):
                        result["posts"].sort(key=self.sortReads,reverse=True)
                    elif(direction == "asc" or direction == None):
                        result["posts"].sort(key=self.sortReads)
                    else:
                        return jsonify(self.dir_error),400
                elif(sortBy == "likes"):
                    if(direction == "desc"):
                        result["posts"].sort(key=self.sortLikes,reverse=True)
                    elif(direction == "asc" or direction == None):
                        result["posts"].sort(key=self.sortLikes)
                    else:
                        return jsonify(self.dir_error),400
                elif(sortBy == "popularity"):
                    if(direction == "desc" ):
                        result["posts"].sort(key=self.sortPop,reverse=True)
                    elif(direction == "asc" or direction == None):
                        result["posts"].sort(key=self.sortPop)
                    else:
                        return jsonify(self.dir_error),400
                else:
                    return jsonify(self.sort_error),400
        else:
           return jsonify(self.tag_error),400

        return result