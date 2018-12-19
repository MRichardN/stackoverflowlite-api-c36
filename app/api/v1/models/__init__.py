
from app.api.v1.views import queston_views

question_list=[{
    "id": 1,
    "title": "Error handlers",
    "description": "which id the custom  handler for 404 errors?",
    "date_posted": "1800hrs"
    },
     {
        "id": 2,
        "title": "Flask",
        "description": "How do i install flask in python",
        "answer": 1,
        "date_posted": "1900hrs"
        }]

answer_list = [{
    "id": 1,
    "updated_answer": "There are varoius ways of handling errors",
    "date_posted": "1800hrs",
    "question_id": 1
    },
    {
        "id": 2,
        "updated_answer": " Using 404 custom error handlers",
        "date_posted": "2200hrs",
        "question_id": 1
        },
        {
            "id": 3,
            "updated_answer": "Using package called pip for python. $ pip install flask",
            "date_posted": "0800hrs",
            "question_id": 2
            }
        ]



