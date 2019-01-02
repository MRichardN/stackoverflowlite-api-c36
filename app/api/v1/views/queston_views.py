
import datetime
from flask import Blueprint, request, jsonify, abort, make_response 
from app.api.v1.models.questions_model import Question
from app.api.v1.models.answer_model import Answer
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

@version1.route('/api/v1/questions/', methods=["GET","POST"])
def get_all_questions():
    """
    View all questions.
    """
    if question:
        #for quiz in question.show_questions():
            #retrieve number of answers
            #quiz["answer"] = len(answer.show_answers(quiz["id"]))
        return jsonify({"Questions": question.show_questions()}), 200
    abort(404)

@version1.route('/api/v1/questions/<int:question_id>/', methods=['GET','POST','PUT','DELETE'])
def get_a_specific_question(question_id):
    """
    Get a specific question.
    """
    if request.method == 'GET':
        qn_list = question.show_questions()
        quiz = [quiz for quiz in qn_list if quiz["id"] == question_id]
        if quiz:
            quiz_answers = answer.show_answers(quiz[0]["id"])
            quiz[0]["answers"] = quiz_answers
            return jsonify({"Question": quiz}), 200
        abort(404)
    elif request.method == "POST":
        if not request.json or not "updated_answer" in request.json:
            abort(404)
        new_answer = {
            "id": answer_list[-1]["id"]+1,
            "updated_answer": request.json["updated_answer"],
            "date_posted":"1900hrs",
            "question_id": question_id
        }
        answer.add_answer(new_answer)
        return jsonify({"Answer":new_answer})


@version1.route('/api/v1/add_question/', methods=["POST"])
def post_question():
    """
    Post a question.
    """
    if not request.json or not 'title' in request.json:
        abort(400)
    post_qn = {
    'id': question_list[-1]['id'] + 1,
    'title': request.json['title'],
    'description': request.json['description'],
    'date_posted': datetime.datetime.now(),
    "answer": 0
    }
    question.add_question(post_qn)
    return jsonify({'question': post_qn}), 201        


@version1.route('/api/v1/update_question/<int:question_id>/', methods=["PUT"])
def update_question(question_id):
    """
    Update a question.
    """
    if not request.json:
          abort(400)
    if 'title' in request.json and type(request.json['title']) != str:
         abort(400)
    if 'description' in request.json and type(request.json['description']) is not str:
        abort(400)
    current_question = [current_question for current_question in question_list if current_question["id"]==question_id]
    if current_question:
        title = request.json.get('title', current_question[0]["title"])
        description = request.json.get('description', current_question[0]['description'])
        date_posted = datetime.datetime.now()
        updated_question = question.update_question(question_id, title, description, date_posted)
        return jsonify({"Question": updated_question}), 201
    abort(404)
    
@version1.route('/api/v1/delete_question/<int:question_id>', methods=['DELETE'])
def delete_question(question_id):
    """
    Delete a question.
    """
    if question.delete_question(question_id):
        return jsonify({"Success": "Question deleted successfully"}), 200
    abort(404)






