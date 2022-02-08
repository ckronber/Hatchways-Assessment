from flask import Flask,request,jsonify
from flask_restful import Api
from models.posts import user_posts
from controllers.getPosts import postRequests
from testing import testResult

app = Flask(__name__)
api = Api(app)
my_request = postRequests()

@app.route('/test')
async def testSolution():
    myTest = testResult()
    myTest.compare_solutions()
    #if statement to check whether the test results print errors
    if(myTest.defaultTestResult().printErrors() == None):
        return jsonify({"errors":"None"})
    else:
        return jsonify(myTest.defaultTestResult().printErrors())

@app.route('/cache')
async def get_cahce():
    if(my_request.cache_store is None):
        return jsonify({"storage":"Empty"})
    return jsonify({"Current Cache":my_request.cache_store}),200

@app.route('/ping')
async def get_ping():
    value = {"success":"true"}
    return value

@app.route('/posts')
async def get_query_string():
    args = request.args

    #checking for more arguments than there should be
    if(len(args) > 3):
        return {"error":"Too many Arguments"},400

    if "tags" in args.keys():
        if "sortBy" in args.keys():
            if"direction" in args.keys():
                get_post = await my_request.get(args["tags"],args["sortBy"],args["direction"])
                return get_post,200
            else:
                get_post = await my_request.get(args["tags"],args["sortBy"])
                return  get_post,200
        else:
            if "direction" in args.keys():
                return  {"error":"direction should not be used here"}
            else:
                get_post = await my_request.get(args["tags"])
                return get_post,200
    else: 
        return my_request.tag_error,400

if __name__ == "__main__":
    app.run(host='localhost',port = 5000,debug=True)