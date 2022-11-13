import unittest
from Tree import Tree
from tinydb import TinyDB, Query

#https://docs.python.org/3.8/library/unittest.html
class TestTreeMethods(unittest.TestCase):
   
      
    tree_1 = Tree(ident=100,
        coordinates=(12,12), 
        species = "Bamboo Bamboozle",
        address='Highfield Campus')
    
    tree_2 = Tree(ident=150,
        coordinates=(13,13),
        species = "Bamboo Bambara",
        address='Avenue Campus')
    
    tree_3 = Tree(ident=180,
      coordinates=(14,14),
      species = "Bamboo Bambara",
      address='That fancy building in town we bought from Solent Uni')


    def test_commit_tree(self):
      Tree.commit_tree(self.tree_1)
      Tree.commit_tree(self.tree_2)
      Tree.commit_tree(self.tree_3)
      self.assertEqual(len(Tree.tree_collection),3)

    #SetUp method executed before each test
    #https://docs.python.org/3/library/unittest.html#unittest.TestCase.setUp
    def setUp(self):
      Tree.tree_collection.truncate()

    #tearDown method executed before each test
    #https://docs.python.org/3/library/unittest.html#unittest.TestCase.setUp
    def tearDown(self):
      Tree.tree_collection.truncate()
      

#Main to execute the tests
if __name__ == '__main__':
    unittest.main()

  
