from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


class VideoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    views = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Video\tname: {name}\tviews= {views}\tlikes = {likes}"


db.create_all()

video_put_args = reqparse.RequestParser()
video_put_args.add_argument(
    "name", type=str, help="You didn't provide a name", required=True)
video_put_args.add_argument(
    "views", type=int, help="You didn't provide views", required=True)
video_put_args.add_argument(
    "likes", type=int, help="You didn't provide likes", required=True)

resource_fields = {
    "id": fields.Integer,
    "name": fields.String,
    "views": fields.Integer,
    "likes": fields.Integer
}


class Video(Resource):
    @marshal_with(resource_fields)
    def get(self, video_id):
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, message="Could not find")
        return result

    @marshal_with(resource_fields)
    def put(self, video_id):
        args = video_put_args.parse_args()

        result = VideoModel.query.filter_by(id=video_id).first()
        if result:
            abort(409, message="Entry already exists")

        video = VideoModel(
            id=video_id, name=args["name"], views=args["views"], likes=args["likes"])
        db.session.add(video)
        db.session.commit()
        return video, 201

    def delete(self, video_id):
        return "", 204


#api.add_resource(Video, "/video/<int:video_id>")


class helloWorld(Resource):
    @marshal_with(resource_fields)
    def get(self):
        result = {"server return": "Hello World"}
        return result


api.add_resource(helloWorld, "/helloworld")

if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5000, debug=True)
