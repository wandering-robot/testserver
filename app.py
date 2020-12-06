from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


# class VideoModel(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     views = db.Column(db.Integer, nullable=False)
#     likes = db.Column(db.Integer, nullable=False)

#     def __repr__(self):
#         return f"Video\tname: {name}\tviews= {views}\tlikes = {likes}"


# db.create_all()

# video_put_args = reqparse.RequestParser()
# video_put_args.add_argument(
#     "name", type=str, help="You didn't provide a name", required=True)
# video_put_args.add_argument(
#     "views", type=int, help="You didn't provide views", required=True)
# video_put_args.add_argument(
#     "likes", type=int, help="You didn't provide likes", required=True)

# resource_fields = {
#     "id": fields.Integer,
#     "name": fields.String,
#     "views": fields.Integer,
#     "likes": fields.Integer
# }


# class Video(Resource):
#     @marshal_with(resource_fields)
#     def get(self, video_id):
#         result = VideoModel.query.filter_by(id=video_id).first()
#         if not result:
#             abort(404, message="Could not find")
#         return result

#     @marshal_with(resource_fields)
#     def put(self, video_id):
#         args = video_put_args.parse_args()

#         result = VideoModel.query.filter_by(id=video_id).first()
#         if result:
#             abort(409, message="Entry already exists")

#         video = VideoModel(
#             id=video_id, name=args["name"], views=args["views"], likes=args["likes"])
#         db.session.add(video)
#         db.session.commit()
#         return video, 201

#     def delete(self, video_id):
#         return "", 204


# api.add_resource(Video, "/video/<int:video_id>")

################################################################################################

# ensure solutions are sent with the proper things
solution_put_args = reqparse.RequestParser()
solution_put_args.add_argument(
    "userName", type=str, help="Did not supply user's name")
solution_put_args.add_argument(
    "userSolution", type=str, help="did not supply solution body")

# ensure solutions get upvoted
problem_put_args = reqparse.RequestParser()
problem_put_args.add_argument(
    "problemId", type=int, help="did not identify problem to upvote")


# ensure problems are added
company_put_args = reqparse.RequestParser()
company_put_args.add_argument(
    "problem", type=str, help="did not supply problem")


class ProblemModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    compName = db.Column(db.String(100), nullable=False)
    probID = db.Column(db.Integer, nullable=False)
    probStartTime = db.Column(db.Date)
    soluID = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Video\tname: {name}\tviews= {views}\tlikes = {likes}"


db.create_all()

# code for company wide view to see all the problems


class companyView(Resource):
    def get(self, companyName):
        result = {"Company Name": companyName}
        return result

    def put(self, companyName):
        args = company_put_args.parse_args()
        return args


api.add_resource(companyView, "/<string:companyName>/",
                 "/<string:companyName>")


# code for the problem view to see all the solutions


class problemView(Resource):
    def get(self, companyName, probNum):
        result = {"Company Name": companyName,
                  "Problem id": probNum}
        return result

    def put(self, companyName, probNum):
        args = problem_put_args.parse_args()
        return args


api.add_resource(problemView, "/<string:companyName>/<int:probNum>")


# code for the solution view to see you enter your solution


class solutionView(Resource):
    def get(self, companyName, probNum, solNum):
        result = {"Company Name": companyName,
                  "Problem id": probNum,
                  "Solution id": solNum}
        return result

    def put(self, companyName, probNum, solNum):
        args = solution_put_args.parse_args()
        return args


api.add_resource(
    solutionView, "/<string:companyName>/<int:probNum>/<int:solNum>")


if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5000, debug=True)
