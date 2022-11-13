import unittest
from User import User
from tinydb import TinyDB, Query

#https://docs.python.org/3.8/library/unittest.html
class TestUsermethods(unittest.TestCase):
 
    user1 = User("TreeHugger1")
    user2 = User("TreeHugger2") 
    user3 = User("TreeHugger3") 

    def test_commit_user(self):
      User.commit_user(self.user1)
      User.commit_user(self.user2)
      User.commit_user(self.user3)
      self.assertEqual(len(User.user_collection),3)

    #SetUp method executed before each test
    #https://docs.python.org/3/library/unittest.html#unittest.TestCase.setUp
    def setUp(self):
      User.user_collection.truncate()

    #tearDown method executed before each test
    #https://docs.python.org/3/library/unittest.html#unittest.TestCase.setUp
    def tearDown(self):
      User.user_collection.truncate()


#Main to execute the tests
if __name__ == '__main__':
    unittest.main()

  
