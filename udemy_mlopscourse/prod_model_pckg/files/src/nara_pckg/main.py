from typing import Optional

from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from os import environ as env
from pyexpat.errors import messages

app = Flask(__name__)
api=Api(app)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database.db'
db = SQLAlchemy(app)

class VideoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100),nullable=False) #creating cols
    views = db.Column(db.Integer,nullable=False)
    likes = db.Column(db.Integer,nullable=False)

    def __repr__(self):
        return f"Video(name={name},views={views},likes={likes})"


db.create_all()


video_put_args=reqparse.RequestParser()
video_put_args.add_argument("name",type=str,required=True,help="Name of video")
video_put_args.add_argument("views",type=int,required=True,help="views of the video")
video_put_args.add_argument("likes",type=int,required=True,help="likes on the video")

video_update_args=reqparse.RequestParser()
video_update_args.add_argument("name",type=str,help="Name of video is required")
video_update_args.add_argument("views",type=int,help="views of the video is required")
video_update_args.add_argument("likes",type=int,help="likes on the video is required")

videos= {}

def abort(video_id):
    if video_id not in videos:
        abort(404)

def abort_if_exists(video_id):
    if video_id not in videos:
        abort(409)




resource_fields = {
    "id":fields.String(),
    "name":fields.String(),
    "views":fields.Integer(),
    "likes":fields.Integer()

}

class Video(Resource):
    @marshal_with(resource_fields)
    def get(self,video_id:int):
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404,messages="video does not exist")
        return result


    @marshal_with(resource_fields)
    def put(self,video_id):
        args = video_put_args.parse_args()
        result = VideoModel.query.filter_by(id=video_id).first()
        if result:
            abort(404,messages="video already exist")

        video = VideoModel(id=video_id,name=args["name"],views=args["views"],likes=args["likes"])
        db.session.add(video)
        db.session.commit()

        return video,201


    def delete(self,video_id):
        result = VideoModel.query.filter_by(id=video_id).first()

        db.session.delete(result)
        db.session.commit()
        return f"video{video_id} deleted",204

    @marshal_with(resource_fields)
    def patch(self,video_id):
        args = video_update_args.parse_args()
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404,messages="video doesnt exist")
        if "name" in args:
            result.name=args["name"]
        if "views" in args:
            result.views=args["views"]
        if "likes" in args:
            result.likes=args["likes"]

        db.session.add(result)
        db.session.commit()

        return result,200




#api.add_resource(HelloWorld,"/helloworld/<string:name>")

api.add_resource(Video,'/video/<int:video_id>')



if __name__=='__main__':
    app.run(debug=True)



