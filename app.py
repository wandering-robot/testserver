from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

import json
from datetime import datetime

app = Flask(__name__)
cors = CORS(app)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


# ensure solutions are sent with the proper things
solution_post_args = reqparse.RequestParser()
solution_post_args.add_argument(
    "userName", type=str, help="Did not supply user's name")
solution_post_args.add_argument(
    "userSolution", type=str, help="did not supply solution body")

# metadata for solutions
problem_post_args = reqparse.RequestParser()
problem_post_args.add_argument(
    "problemId", type=int, help="did not identify problem to upvote")


# ensure problems are upvotes
problem_put_args = reqparse.RequestParser()
problem_put_args.add_argument(
    "problemId", type=int, help="did not identify problem to upvote")

# ensure problems are added
company_put_args = reqparse.RequestParser()
company_put_args.add_argument(
    "problem", type=str, help="did not supply problem")

### code for the company wide view to see the problems ###


class companyView(Resource):
    ''' code for company wide view to see all the problems'''

    def get(self, companyName):
        '''would load all the problems in the company's database'''
        result = {"Company_Name": companyName}
        return result


api.add_resource(companyView, "/<string:companyName>/",
                 "/<string:companyName>")


### code for the problem view to see all the solutions ###

def get_data(filename):
    data_list = []
    with open(filename, 'r') as file:
        for line in file:
            data_list.append(line)
    return data_list


def jsonify(data_list):
    data = {}
    for line in data_list:
        line = line.strip('\n')
        line_list = line.split('\t')
        if len(line_list) > 1:
            data[line_list[0]] = {
                "name": line_list[1], "solution": line_list[2]}
    return data


class problemView(Resource):
    '''code to see all the proposed solutions to a problem'''

    def get(self, companyName, probNum):
        '''loads all the solutions to a problem in the database'''
        if probNum == 1:
            result = get_data('data1.txt')
        elif probNum == 2:
            result = get_data('data2.txt')
        result = jsonify(result)
        return {"data": result}

    def post(self, companyName, probNum):
        '''creates a new solution'''
        args = problem_post_args.parse_args()   # "problemId"
        print(f'\n{args}\n')  # not sure if I should be doing things here
        return args

    def put(self, companyName, probNum):
        '''upvotes a solution'''
        args = problem_post_args.parse_args()   # "problemId"
        print(f'\n{args}\n')
        if probNum == 1:
            solution_entry = Problem1Database.query.filter_by(
                ID=probNum).first()  # not sure if I can access this like this
            solution_entry.soluLikes += 1
        elif probNum == 2:
            solution_entry = Problem2Database.query.filter_by(
                ID=probNum).first()  # not sure if I can access this like this
            solution_entry.soluLikes += 1
        db.session.commit()
        return 200


api.add_resource(problemView, "/<string:companyName>/<int:probNum>")


### code for the solution view to see you enter your solution ###
def sol_not_in(solNum, fileName):
    data_list = get_data(fileName)
    json_list = jsonify(data_list)
    for key in json_list.keys():
        print(key, solNum)
        if key == solNum:
            return False
    return True


class solutionView(Resource):
    def get(self, companyName, probNum, solNum):
        result = {"Company_Name": companyName,
                  "Problem_id": probNum,
                  "Solution_id": solNum}
        return result

    def post(self, companyName, probNum, solNum):
        args = solution_post_args.parse_args()
        if probNum == 1:
            if sol_not_in(solNum, "data1.txt"):
                args = solution_post_args.parse_args()      # "userName" "userSolution"
                with open('data1.txt', 'a') as file:
                    file.write(
                        f'{solNum}\t{args["userName"]}\t{args["userSolution"]}\n')
        elif probNum == 2:
            if sol_not_in(solNum, "data2.txt"):
                print("**********")
                args = solution_post_args.parse_args()      # "userName" "userSolution"
                with open('data2.txt', 'a') as file:
                    file.write(
                        f'{solNum}\t{args["userName"]}\t{args["userSolution"]}\n')
        print(f'\n{args}\n')
        return json.dumps(args)


api.add_resource(
    solutionView, "/<string:companyName>/<int:probNum>/<int:solNum>")


if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5000, debug=True)
