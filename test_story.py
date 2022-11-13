import unittest
from Story import Story
from tinydb import TinyDB, Query

#https://docs.python.org/3.8/library/unittest.html
class TestStoryMethods(unittest.TestCase):
   
      
 
    def test_commit_story(self):
      pass

    #SetUp method executed before each test
    #https://docs.python.org/3/library/unittest.html#unittest.TestCase.setUp
    def setUp(self):
      Story.story_collection.truncate()

    #tearDown method executed before each test
    #https://docs.python.org/3/library/unittest.html#unittest.TestCase.setUp
    def tearDown(self):
      Story.story_collection.truncate()
      

#Main to execute the tests
if __name__ == '__main__':
    unittest.main()

  
