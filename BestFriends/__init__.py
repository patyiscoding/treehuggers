import logging
import azure.functions as func
import json

def calc_best_friend(tree_id, stories):
    """
    Input: A tree
    Output: The user that has written most stories involving the input Tree.
    """
    users = {}

    for item in stories:
      username = item['username']
      if int(tree_id) == int(item['tree_id']):
        if username in users:
          users[username] = users[username] + 1
        else:
          users[username] = 1
    print("best friends: ", users)

    best_friend = max(users, key=users.get)
    return best_friend


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Computing Best Friends in the Cloud.')

    stories = req.get_json().get('stories')
    tree_id = req.get_json().get('tree_id')
    
    best_friend = calc_best_friend(tree_id, stories)

    return func.HttpResponse(body=json.dumps(best_friend), status_code = 200)
