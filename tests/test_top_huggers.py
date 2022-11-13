import unittest
import json
# Read this: https://requests.readthedocs.io/en/latest/user/quickstart/#make-a-request
import requests 

import azure.functions as func
from TopHuggers import main

class TestFunction(unittest.TestCase):
    def test_top_huggers(self):
        # Instead of a mock HTTP request.
        # We make a real HTTP request, passing our mock stories as parameters
        payload = {'stories': 
                [{"id": "10", "username": "Bob", "tree_id": 100, "text": "Hello Tree", "date": "2022-10-20"},
                {"id": "11", "username": "Bob", "tree_id": 110, "text": "Hello, other Tree", "date": "2022-10-20"},
                {"id": "12", "username": "Alice", "tree_id": 110, "text": "Howdy, Tree", "date": "2022-10-20"}
                ]}


        resp = requests.get(
                #This is the URL of the function deployed in the local development server
                'http://localhost:7071/api/tophuggers', 
                #send payload as JSON
                json = payload)

        # This converts the body of the response (bytes) back into a JSON dictionary 
        top_huggers = resp.json() 

        # DONE: Modify this assert to test the tophuggers function
        self.assertEqual(len(top_huggers), 2)
        self.assertEqual(top_huggers['Bob'],2)
        self.assertEqual(top_huggers['Alice'],1)
