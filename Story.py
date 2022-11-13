from tinydb import TinyDB, Query, where
from tinydb.operations import delete
import collections

class Story():
  story_collection = TinyDB("story_collection.json")
  Story = Query()

  def __init__(self,story_id,username,tree_id,text,story_date):  
    self.story_id = story_id
    self.username = username
    self.tree_id = tree_id
    self.text = text
    self.date = story_date

  # Output: string representation of Story
  def __str__(self):
    return """This is a story with
    id = {}
    username={}
    tree_id={}
    text = {}
    date = {}
    """.format(self.story_id,self.username,self.tree_id,self.text, self.date)

  @classmethod
  def commit_story(cls,story):
    """
    Input: An instance of a Story
    Output: The Story is persisted in database
    """
    story_list = cls.story_collection.search(where('story_id') == story.story_id)

    print(story)
    if len(story_list) == 0:
      cls.story_collection.insert({"story_id" : story.story_id,
                           "username" : story.username,
                           "tree_id" : story.tree_id,
                           "text" : story.text,
                           "date" : story.date})  
    else:
      raise ValueError("Inserting a story with id" + story.story_id + "that already exists") 
    pass

  @classmethod
  def top_huggers(cls):
    """
    Output: Dictionary user.username -> number of stories this user has
    Hint: Create some stories so you can create a meaningful test case
    """
    users = {}
    for item in cls.story_collection:
      username = item['username']
      if username in users.keys():
        users[username] = users[username] + 1
      else:
        users[username] = 1
        
    return users

  @classmethod
  def best_friend(cls,tree):
    """
    Input: A tree
    Output: The user that has written most stories involving the input Tree.
    """
    tree_id = tree.id
    users = {}
    for item in cls.story_collection:
      username = item['username']
      if int(tree_id) == int(item['tree_id']):
        if username in users:
          users[username] = users[username] + 1
        else:
          users[username] = 1
    print("best friends: ", users)

    users = max(users, key=users.get)
    return users