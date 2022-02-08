from flask_restful import Resource
from models.posts import user_posts
from flask import json,jsonify
import requests

class postRequests(Resource):
    def __init__(self):
        self.tag_error = {"error":"tags parameter is required"}
        self.sort_error = {"error":"sortBy paremeter is invalid"}
        self.dir_error = {"error":"direction parameter is invalid"}
        self.cache_store = {}   #dictionary to store values from individual tags
    
    def sortId(self,e):
        return e['id']
    def sortReads(self,e):
        return e['reads']
    def sortLikes(self,e):
        return e['likes']
    def sortPop(self,e):
        return e['popularity']

    async def deserialize(self,myInput):
        schema = user_posts(many=True)
        result = schema.load(myInput)
        return json(result)

    async def serialize(self,input_posts):    
        mySchema = user_posts(many=True)
        j_result = mySchema.dump(input_posts)
        return j_result

    async def check_cache(self,tag:str):
        if(tag in self.cache_store.keys()):
            print("brought from cache")
            return self.cache_store[tag]
        else:
            print("stored to cache")
            #self.tag_store.append(tag)
            get_data = requests.get('https://api.hatchways.io/assessment/blog/posts',params={"tag":tag})
            json_data = get_data.json()
            self.cache_store[tag] = json_data["posts"]
            return json_data["posts"]

    async def get(self,tags:str,sortBy:str = None,direction:str = None):
        #changes string input to list of strings
        post_tags = tags.split(',')
        post_list = []
        after_sort_list = []

        if(post_tags):
            for tag in post_tags:
                post_list += await self.check_cache(tag)

            #checking for duplicates in the list
            for listItem in post_list:
                if(listItem not in after_sort_list):
                    after_sort_list.append(listItem)

            result = {"posts": after_sort_list}
            
            #Section that checks and directs sortBy and direction values
            if(sortBy):
                if(sortBy == "id"):
                    if(direction == "desc"):
                        result["posts"].sort(key=self.sortId,reverse=True)
                    elif(direction == "asc" or direction == None):
                        result["posts"].sort(key=self.sortId)
                    else:
                        return self.dir_error,400
                elif(sortBy == "reads"):
                    if(direction == "desc"):
                        result["posts"].sort(key=self.sortReads,reverse=True)
                    elif(direction == "asc" or direction == None):
                        result["posts"].sort(key=self.sortReads)
                    else:
                        return self.dir_error,400
                elif(sortBy == "likes"):
                    if(direction == "desc"):
                        result["posts"].sort(key=self.sortLikes,reverse=True)
                    elif(direction == "asc" or direction == None):
                        result["posts"].sort(key=self.sortLikes)
                    else:
                        return self.dir_error,400
                elif(sortBy == "popularity"):
                    if(direction == "desc" ):
                        result["posts"].sort(key=self.sortPop,reverse=True)
                    elif(direction == "asc" or direction == None):
                        result["posts"].sort(key=self.sortPop)
                    else:
                        return self.dir_error,400
                else:
                    return self.sort_error,400

        #if no tag return a 400 error
        else:
           return self.tag_error,400


        return jsonify(result)