import requests
from flask import Flask,jsonify,url_for,request,json
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
my_request = postRequests()

#@app.route('ping')
@app.route('/posts')
def get_query_string():
    args = request.args
    if(len(args) > 3):
        return 404

    if "tag" in args.keys():
        if "sortBy" in args.keys():
            if"direction" in args.keys():
                return my_request.get(args["tag"],args["sortBy"],args["direction"])
            else:
                return my_request.get(args["tag"],args["sortBy"])
        else:
            return my_request.get(args["tag"])
    else:
        return 404

    """
    if(args["tag"] and args["sortBy"]):
        return my_request.get(str(args["tag"]),str(args["sortBy"]),str(args["direction"]))
    elif(args["tag"] and args["sortBy"]):
        return my_request.get(str(args["tag"]),str(args["sortBy"]))
    elif(args):
        return my_request.get(str(args["tag"]))
    """

if __name__ == "__main__":
    app.run(host='localhost',port = 5000,debug=True)