import logging
import azure.functions as func
import json

def calc_top_huggers(collection):
    """
    Output: Dictionary user.username -> number of stories this user has
    Hint: Create some stories so you can create a meaningful test case
    """
    users = {}
    for item in collection:
      username = item['username']
      if username in users.keys():
        users[username] = users[username] + 1
      else:
        users[username] = 1
        
    return users

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Computing Top Huggers in the Cloud')

    # In the Request on the unit test, we sent a params dictionary
    # This Function received it as the req parameter
    stories = req.get_json().get('stories')

    top_huggers = {}
    
    # DONE: Adapt code from EarthPrototype to compute Top Huggers into top_huggers dictionary
    top_huggers = calc_top_huggers(stories)
    
    # We convert the result dictionary into JSON format and send it as a String (the dumps method)
    return func.HttpResponse(body=json.dumps(top_huggers),
            # HTTP Status Code
            # Read this: https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
            status_code = 200)

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