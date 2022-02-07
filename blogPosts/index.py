from flask import Flask,request,jsonify,json
from flask_restful import Api
from pprint import pprint
from models.posts import user_posts
from controllers.getPosts import postRequests
import asyncio

app = Flask(__name__)
api = Api(app)
my_request = postRequests()

@app.route('/cache')
def get_cahce():
    return jsonify(my_request.cache_storage),200

@app.route('/ping')
def get_ping():
    value = {"success":"true"}
    return jsonify(value)

@app.route('/posts')
def get_query_string():
    args = request.args
    if(len(args) > 3):
        return jsonify({"error":"Too many Arguments"}),400

    if "tag" in args.keys():
        if "sortBy" in args.keys():
            if"direction" in args.keys():
                return my_request.get(jsonify(args["tag"],args["sortBy"],args["direction"])),200
            else:
                return my_request.get(jsonify(args["tag"],args["sortBy"])),200
        else:
            if "direction" in args.keys():
                return jsonify({"error":"direction should not be used here"})
            else:
                return jsonify(my_request.get(args["tag"])),200
    else: 
        return jsonify(my_request.tag_error),400

if __name__ == "__main__":
    app.run(host='localhost',port = 5000,debug=True)