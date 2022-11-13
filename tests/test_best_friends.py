import unittest
import json
# Read this: https://requests.readthedocs.io/en/latest/user/quickstart/#make-a-request
import requests 
import os
import azure.functions as func
from BestFriends import main

print("os: ", os.environ)

class TestFunction(unittest.TestCase):
    def test_best_friends(self):
        local_URI = os.environ["local_URI"]
        # Instead of a mock HTTP request.
        # We make a real HTTP request, passing our mock stories as parameters
        payload = {'stories': 
                [{"id": "10", "username": "Bob", "tree_id": 100, "text": "Hello Tree", "date": "2022-10-20"},
                {"id": "11", "username": "Bob", "tree_id": 110, "text": "Hello, other Tree", "date": "2022-10-20"},
                {"id": "12", "username": "Alice", "tree_id": 110, "text": "Howdy, Tree", "date": "2022-10-20"}
                ], 'tree_id': 100}


        resp = requests.get(local_URI + 'bestfriends', json = payload)

        # This converts the body of the response (bytes) back into a JSON dictionary 
        best_friend = resp.json() 

        # actual testing
        self.assertEqual(best_friend,'Bob')