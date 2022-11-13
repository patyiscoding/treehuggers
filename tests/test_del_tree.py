import unittest
import json
# We use the requests library to communicate with servers programatically 
# You should install it in your virtual environment using pip install requests
# Read this: https://requests.readthedocs.io/en/latest/user/quickstart/#make-a-request
import requests 

import azure.functions as func
import azure.cosmos as cosmos
# Use this code block to access settings from a config.py
import config
db_URI = config.settings['db_URI']
db_id = config.settings['db_id']
db_key = config.settings['db_key']
trees_cont = config.settings['trees_container']

# Tests outside of the development server
# Therefore, environment variables are not available
#import os 
#print(os.environ)
#db_URI = os.environ['db_URI']
#db_id = os.environ['db_id']
#db_key = os.environ['db_key']
#trees_cont = os.environ['trees_container']

class TestFunction(unittest.TestCase):

    client = cosmos.cosmos_client.CosmosClient(db_URI, db_key )
    db_client = client.get_database_client(db_id)
    trees_container = db_client.get_container_client(trees_cont)

    def setUp(self) -> None:
        #ensure container is empty before running any test
        all_trees = self.trees_container.read_all_items()
        for tree in all_trees:
            self.trees_container.delete_item(tree['id'],tree['id'])

    def test_delete_tree(self):
        # Test dependency: add_tree must work to test correctly delete_tree
        payload = {'tree' : { 'tree_id' : 100,
                    'coordinates' : {'lat' : 20 , 'lon' : 40},
                    'address' : 'Highfield Campus',
                    'species' : 'Oak'
                } }
        resp = requests.get('http://localhost:7071/api/AddTree',json = payload)
        self.assertEqual(resp.json()['msg'],'OK')
        
        payload = {'tree_id' : 100 }
        resp = requests.get('http://localhost:7071/api/DeleteTree',json = payload)
        #Database empty
        all_trees = list(self.trees_container.read_all_items())
        self.assertEqual(len(all_trees),0)

        def test_delete_tree_non_existent(self):
            # Test dependency: add_tree must work to test correctly delete_tree
            payload = {'tree_id' : 555 }
            resp = requests.get('http://localhost:7071/api/DeleteTree',json = payload)
            #Database should be empty
            all_trees = list(self.trees_container.read_all_items())
            self.assertEqual(len(all_trees),0)
            #and we received the right message
            self.assertEqual(resp.json()['msg'],"Does not exist")
            