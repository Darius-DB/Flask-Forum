from flaskforum.models import User, Question, Answer
from flaskforum import app
from flask_restful import Api, Resource, marshal_with, fields

api = Api(app)

user_resource_fields = {
    'id': fields.Integer,
    'email': fields.String,
    'username': fields.String,
    'image_file': fields.String
}

question_resource_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'content': fields.String,
    'tag_1': fields.String,
    'tag_2': fields.String,
    'date_added': fields.DateTime,
    'user_id': fields.Integer
}

answer_resource_fields = {
    'id': fields.Integer,
    'content': fields.String,
    'date_added': fields.DateTime,
    'user_id': fields.Integer,
    'question_id': fields.Integer
}

class AllUsers(Resource):
    @marshal_with(user_resource_fields)
    def get(self):
        result = User.query.all()
        return result

class SingleUser(Resource):
    @marshal_with(user_resource_fields)
    def get(self, user_id):
        result = User.query.filter_by(id=user_id).first()
        return result

class AllQuestions(Resource):
    @marshal_with(question_resource_fields)
    def get(self):
        result = Question.query.all()
        return result

class SingleQuestion(Resource):
    @marshal_with(question_resource_fields)
    def get(self, question_id):
        result = Question.query.filter_by(id=question_id).first()
        return result

class AllAnswers(Resource):
    @marshal_with(answer_resource_fields)
    def get(self):
        result = Answer.query.all()
        return result

class SingleAnswer(Resource):
    @marshal_with(answer_resource_fields)
    def get(self, answer_id):
        result = Answer.query.filter_by(id=answer_id).first()
        return result

api.add_resource(AllUsers, '/api/v1/resource/users/all')
api.add_resource(SingleUser, '/api/v1/resource/users/<int:user_id>')

api.add_resource(AllQuestions, '/api/v1/resource/questions/all')
api.add_resource(SingleQuestion, '/api/v1/resource/questions/<int:question_id>')

api.add_resource(AllAnswers, '/api/v1/resource/answers/all')
api.add_resource(
    SingleAnswer, '/api/v1/resource/answers/<int:answer_id>')
