#app/main/models.py


class Question(object):
    """
    Question model.
    """
    def __init__(self, question_list):
        """
        Initialize questions list.
        """
        self.question_list = question_list

    def show_questions(self):
        """
        Show the questions.
        """
        return self.question_list

    def add_question(self, question):
        """
        Add questions to the list.
        """
        self.question_list.append(question)

    def update_question(self, index, title, description, date_posted):
        """
        Update a question.
        """
        new_question = [new_question for new_question in self.question_list if new_question["id"] == index]
        if new_question:
            new_question[0]["title"] = title
            new_question[0]["description"] = description
            new_question[0]["date_posted"] = date_posted
            return new_question[0]

    def delete_question(self, index):
        """
        Delete questions.
        """
        del_question = [del_question for del_question in self.question_list if del_question["id"] == index]
        if del_question:
            self.question_list.remove(del_question[0])
            return True

class Answer(object):
    """
        Answers to questions.
    """
    def  __init__(self, answer_list):
        """
        Initialize answers list.
        """
        self.answer_list = answer_list

    def show_answers(self, question_id):
        """
        show  answers.
        """
        answers = [answers for answers in self.answer_list if answers["question_id"] == question_id]
        if answers:
            return answers

    def add_answer(self, answer):
        """
        Add answer to  answer_list.
        """
        self.answer_list.append(answer)
        return answer

    def update_answer(self, answer_id, updated_answer):
        """
        update an existing answer.
        """
        answer=[answer for answer in self.answer_list if answer["id"] == answer_id]
        if answer:
            answer[0]["updated_answer"]=updated_answer
            return answer[0]

    def delete_answer(self, id):
        """
        Delete an answer.
        """
        answer= [answer for answer in self.answer_list if answer["id"] == id]
        if answer:
            self.answer_list.remove(answer[0])
            return True
