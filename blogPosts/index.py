import requests
from flask import Flask,jsonify,url_for,request
from flask_restful import Api
from pprint import pprint
from models.posts import Post,user_posts
from controllers.getPosts import postRequests
from marshmallow import Schema,fields
import json

#myPost = dict(id = 1, author= "Billy Talent", authorid = 2, likes = 123,popularity = .324, reads = 2932,tags = ["health","finance"])
#myPost = requests.get(url="https://api.hatchways.io/assessment/blog/posts", params={"tag":"tech"}).json()

#this_request = postRequests()
#my_request = this_request.get("health")[0]["posts"]

"""
def deserialize(myInput):
    schema = user_posts(many=True)
    result = schema.load(myInput)
    #posts = []
    #for p in myPost["posts"]:
    #    result = schema.load(p)
    #    posts.append(result)
    return result

def serialize(input_posts):    
    mySchema = user_posts(many=True)
    j_result = mySchema.dump(input_posts)
    return j_result

my_out = deserialize(myPost["posts"])
print(my_out)
print("\n\n")
my_in = serialize(my_out)
outdict = {"posts":my_in}
print(outdict)
"""

#results = []
"""
for p in myPost.json():
    result = schema.load(p)
    pprint(result)
    results.append(result)
"""
#pprint(result['id'],indent = 2)

#myPost = postRequests()
#results = myPost.get("health","likes")

#def myFunc(e):
#    return e['id']

#get_data = requests.get(url="https://api.hatchways.io/assessment/blog/posts", params={"tag":"tech"})
#newData = get_data.json()
# newData["posts"].sort(key=myFunc)

#for data in results[0]["posts"]:
#    print(data)

def deserialize(myInput):
    schema = user_posts(many=True)
    result = schema.load(myInput)
    #posts = []
    #for p in myPost["posts"]:
    #    result = schema.load(p)
    #    posts.append(result)
    return result

def serialize(input_posts):    
    mySchema = user_posts(many=True)
    j_result = mySchema.dump(input_posts)
    return j_result


app = Flask(__name__)
api = Api(app)

#@app.route('ping')
@app.route('/posts')
def get_query_string():
    return request.query_string,200
    
if __name__ == "__main__":
    app.run(host='localhost',port = 5000,debug=True)
