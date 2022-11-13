import json
import logging

import azure.functions as func
import azure.cosmos as cosmos
import azure.cosmos.exceptions as exceptions
#import config
#db_URI = config.settings['db_URI']
#db_id = config.settings['db_id']
#db_key = config.settings['db_key']
#trees_cont = config.settings['trees_container']

import os 
db_URI = os.environ['db_URI']
db_id = os.environ['db_id']
db_key = os.environ['db_key']
trees_cont = os.environ['trees_container']

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Inserting a Tree in progress....')

    # Create the needed proxy objects for CosmosDB account, database and tree container
    client = cosmos.cosmos_client.CosmosClient(db_URI, db_key)

    # Create a proxy object to the treehuggers Cosmos DB database
    # Read reference here: https://learn.microsoft.com/en-us/python/api/azure-cosmos/azure.cosmos.databaseproxy?view=azure-python
    db_client = client.get_database_client(db_id)

    # Create a proxy object to the trees container
    # Read reference here: https://learn.microsoft.com/en-us/python/api/azure-cosmos/azure.cosmos.containerproxy?view=azure-python
    trees_container = db_client.get_container_client(trees_cont)


    tree = req.get_json().get('tree')

    # Insert code here to translate from the request with 'tree_id' : int to a JSON with 
    # 'id' :string so you can insert into trees_container
    tree['id'] = str(tree['tree_id'])
    tree.pop('tree_id')

    # Read the documentation of the create_item method and tree
    # https://learn.microsoft.com/en-us/python/api/azure-cosmos/azure.cosmos.containerproxy?view=azure-python#azure-cosmos-containerproxy-create-item
    # Reference on Python exception handling: https://docs.python.org/3.9/tutorial/errors.html

    try:
        # the right create_item call
        # If everything went well return the right response according to specification
        trees_container.create_item(tree)
        return func.HttpResponse(body=json.dumps({"msg": "OK"}))
    except exceptions.CosmosHttpResponseError:
        # Return the right response according to specification when something goes wrong
        # Does this exception matches what we need in the specifications? Yes
        return func.HttpResponse(json.dumps({"msg" : "Tree already exists"}))


    # An alternative to the try-except approach is to query for the item before inserting




"""
name = req.params.get('name')
if not name:
    try:
        req_body = req.get_json()
    except ValueError:
        pass
    else:
        name = req_body.get('name')

if name:
    return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
else:
    return func.HttpResponse(
          "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
          status_code=200
    )
"""