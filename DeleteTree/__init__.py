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
    logging.info('Deleting a Tree in progres....')

    client = cosmos.cosmos_client.CosmosClient(db_URI, db_key)
    db_client = client.get_database_client(db_id)
    trees_container = db_client.get_container_client(trees_cont)

    tree_id = req.get_json().get('tree_id')
    logging.info("Tree to be deleted: %s", tree_id)
    tree_id = str(tree_id)

    try:
        trees_container.delete_item(item=tree_id,partition_key=tree_id)
        return func.HttpResponse(body=json.dumps({"msg": "OK"}))
    except exceptions.CosmosHttpResponseError:
        return func.HttpResponse(json.dumps({"msg" : "The Tree you're trying to delete doesn't exist"}))

