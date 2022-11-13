import unittest
import json
# We use the requests library to communicate with servers programatically 
# You should install it in your virtual environment using pip install requests
# Read this: https://requests.readthedocs.io/en/latest/user/quickstart/#make-a-request
import requests 
import azure.functions as func
import azure.cosmos as cosmos
"""
import config
db_URI = config.settings['db_URI']
db_id = config.settings['db_id']
db_key = config.settings['db_key']
trees_cont = config.settings['trees_container']
"""
#Important for the import name to match the case of the Function folder
#from AddTree import main

import os
db_URI = os.environ['db_URI']
db_id = os.environ['db_id']
db_key = os.environ['db_key']
trees_cont = os.environ['trees_container']

class TestFunction(unittest.TestCase):
    client = cosmos.cosmos_client.CosmosClient(db_URI, db_key)
    db_client = client.get_database_client(db_id)
    trees_container = db_client.get_container_client(trees_cont)

    def test_add_tree(self):
        # Instead of a mock HTTP request.
        # We make a real HTTP request, passing our mock stories as parameters
        payload = {'tree' : { 'tree_id' : 106,
                    'coordinates' : {'lat' : 20 , 'lon' : 40},
                    'address' : 'Highfield Campus',
                    'species' : 'Oak'
                } }


        resp = requests.get(
                #This is the URL of the function deployed in the local development server
                # The URL of the Cloud deployment depends on the URL of the resource group
                'https://treehuggers-pww1u19.azurewebsites.net/api/addtree', 
                #send payload as JSON
                json = payload)

        #To test this function, assuming we start with an empty container
        # we need to assert that only one tree was inserted
        # and the inserted tree corresponds to the payload 
        
        # Create a Proxy object to the Cosmos DB account

        # read reference to read_all_items here: 
        # https://learn.microsoft.com/en-us/python/api/azure-cosmos/azure.cosmos.containerproxy?view=azure-python#azure-cosmos-containerproxy-read-all-items
        # We need to create a list from the iterator to apply len function
        # this line was
        #all_trees = self.trees_container.read_all_items()
        all_trees = list(self.trees_container.read_all_items())
            
        self.assertEqual(len(all_trees),1)
        the_tree_in_the_db = all_trees[0]
        #This test below will fail because the tree in the db comes with the metadata added by
        #CosmosDB. Update this to make the right comparison (field by field, or stripping out the metadata
        #from the tree_in_th_db)
        self.assertEqual(payload['tree'],the_tree_in_the_db)

        #We also need to test that the right message according to specifications has been returned
        # Insert code here to test that we got {'msg' : 'OK'} as expected using self.assertEqual
