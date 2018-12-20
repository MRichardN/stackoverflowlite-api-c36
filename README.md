# stackoverflowlite-api-c36
StackOverflow-lite is a platform where people can ask questions and provide answers.

## Prerequisites
- Python 3.7.0 
- Postman


## Installation
1. Clone this repository :

	```
    $ git clone https://github.com/MRichardN/stackoverflowlite-api-c36.git
    ```

2. CD into the project folder on your machine

	```
    $ cd stack-overflow-lite-api-c36
    ```

3. Create a virtual environment

	```$ python3 -m venv venv
    ```

4. Activate the virtual environment

	```
    $ . venv/bin/activate
    ```

5. Install the dependencies from the requirements file

	```
    $ pip install -r requirements.txt
    $ pip install python-dotenv
    ```

6. Run the application

    ```
    python3 run.py
    ```

## Testing API endpoint

| Endpoint                             | HTTP Verb   | Functionality |
| ------------------------------------ | ----------- | ------------- |
| /api/v1/delete_question/question_id  | DELETE      | Delete a question |
| /api/v1/update_question/question_id/ | PUT         | Update a question
| /api/v1/add_question/                | POST        | Post a question  |
| /api/v1/questions/question_id/       | GET         | Get a specific question |
| /api/v1/questions/                   | GET         | Get all questions   |


## Authors
Mathenge Richard - [MRichardN](https://github.com/MRichardN)

## License
Licensed under [MIT](https://github.com/MRichardN/stackoverflowlite-api-c36/blob/master/LICENSE).

## Acknowledgement
Andela Workshops
