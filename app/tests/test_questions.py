import unittest
import json

from app import create_app


class TestStackOverflow(unittest.TestCase):
    """ """
    def setUp(self):
        self.app = create_app(config_name='testing')
        self.client = self.app.test_client()
        self.questions = {'title':'Python', 'description':'What is TDD'}
        
    
    def test_post_question(self):
        """ Test posting a question."""
        response = self.client.post('/api/v1/add_question/', data=json.dumps(self.questions), content_type = 'application/json')
        self.assertEqual(response.status_code, 201)
        
        

    
    def test_delete_question(self):
        pass
        

    def test_update_question(self):
        """ Test editing a question."""
        #self.client.post('/api/v1/update_question/1/', data=json.dumps(self.questions), content_type='application/json')
        response = self.client.put('/api/v1/update_question/1/', data=json.dumps(self.questions), content_type='application/json')
        self.assertEqual(response.status_code, 200)
       

       

    def test_view_all_questions(self):
        """ Test view_all questions."""
        response = self.client.get('/api/v1/questions/', content_type='application/json')
        self.assertEqual(response.status_code, 200)
        

    def test_view_single_question(self):
        """ Test view a single question."""
        response = self.client.get('/api/v1/questions/1/', data=json.dumps(self.questions), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        

if __name__ == '__main__':
    unittest.main()                    