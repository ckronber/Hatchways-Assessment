from marshmallow import Schema, fields, post_load

class Post():
    def __init__(self,id,author,authorId,likes,popularity,reads,tags):
        self.id = id
        self.author = author
        self.authorId = authorId
        self.likes = likes
        self.popularity = popularity
        self.reads = reads
        self.tags = tags

    def __repr__(self):
        #return "<Author(author={self.author!r})>".format(self=self)
        return f" ID: {self.id}, Author: {self.author}, Reads: {self.reads}, Likes: {self.likes}, Popularity: {self.popularity}, tags: {self.tags}"

class user_posts(Schema):
    id = fields.Int()
    author = fields.Str()
    authorId = fields.Int()
    likes = fields.Int()
    popularity = fields.Float()
    reads = fields.Int()
    tags = fields.List(fields.String())

    @post_load
    def make_post(self,data,**kwargs):
        return Post(**data)