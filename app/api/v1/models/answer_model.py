class Answer:
    """
        This class represents answers to questions.
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
        answers = [answer for answer in self.answer_list if answer["question_id"] == question_id]
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
        answer = [answer for answer in self.answer_list if answer["id"] == answer_id]
        if answer:
            answer[0]["updated_answer"] = updated_answer
            return answer[0]

    def delete_answer(self, _id):
        """
        Delete an answer.
        """
        answer = [answer for answer in self.answer_list if answer["_id"] == _id]
        if answer:
            self.answer_list.remove(answer[0])
            return True
