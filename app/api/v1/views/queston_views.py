
import datetime
from flask import Blueprint, request, jsonify, abort, make_response 
from app.api.v1.models.questions_model import Question, Answer
from app.api.v1.models import question_list, answer_list


version1 = Blueprint("version1", __name__)

question = Question(question_list)
answer=Answer(answer_list)


@version1.errorhandler(404)
def item_not_found(error):
    """
    Custom response to 404 errors.
    """
    return make_response(jsonify({'Failed' : 'Item not found'}), 404)


@version1.errorhandler(400)
def bad_method(error):
    """
    Custom response to 400 errors.
    """
    return make_response(jsonify({'Failed': 'bad request'}))

@version1.route("/api/v1/questions/", methods=["GET","POST"])
def get_all_questions():
    """
    View all questions.
    """
    if question:
        for quiz in question.show_questions():
            #retrieve number of answers
            quiz["answer"]=len(answer.show_answers(quiz["id"]))
        return jsonify({"Questions": question.show_questions()}), 200
    abort(404)








