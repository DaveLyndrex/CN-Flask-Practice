from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class VideoModel(db.Model): 
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable=False)
    views = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return "Video(name = {name}, views = {views}, likes = {likes})"

#db.create_all()
#it would be run once to avoid overiding

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video is required", required=True)
video_put_args.add_argument("views", type=int, help="Views of the video", required=True)
video_put_args.add_argument("likes", type=int, help="Likes of the video", required=True)

#this will resource fields will define the class video model. 
resource_fields = {
    'id' : fields.Integer,
    'name' : fields.String,
    'views' : fields.Integer,
    'likes' : fields.Integer

}

#videos = {}

#def abort_if_video_id_doesnt_exists(video_id):
    #if video_id not in videos:
        #abort(404, message ="Video could not found!")

#def abort_if_video_id_exists(video_id):
    #if video_id in videos:
        #abort(409, message="Video already exists with that ID.")





class Video(Resource):
    @marshal_with(resource_fields)#means that when we return, take the return result(value) and serialize it using resource_fields. It could be a json format
    def get(self, video_id):
        result = VideoModel.query.get(id=video_id)#result is an object. This videomodel.queru gives us an object of an instance of video model
        return result
        #abort_if_video_id_doesnt_exists(video_id)
        #return videos[video_id]

    @marshal_with(resource_fields)
    def put(self, video_id):
        #abort_if_video_id_exists(video_id)
        args = video_put_args.parse_args()#args stores all of the value that we passed in. ... 
        video = VideoModel(id =video_id, name = args['name'], views = args['views'], likes = args['likes'])#Making new object in database....creating new video model
        db.session.add(video)#to make sure that this will add into database. add this object into database session
        db.session.commit()#permanently putting it in
        #print (request.form)
        return video, 201  

    def delete(self, video_id):
        abort_if_video_id_doesnt_exists(video_id)
        del videos[video_id]
        return '', 204 

api.add_resource(Video, "/video/<int:video_id>")

if __name__ == "__main__":
    app.run(debug=True)