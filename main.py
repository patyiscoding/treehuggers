# If you need to check something quickly, use the interpreter
import procedures as pro
from Story import Story
from Tree import Tree

trees_bcn = pro.extract_trees_bcn('data/Trees_Barcelona.json')
print(len(trees_bcn))
"""
Story.commit_story(Story('76543', 'myuser', 1, "text", "10/03/22"))
Story.commit_story(Story('24', 'myuser', 4, "text", "10/03/22"))

Story.commit_story(Story('1341', 'fkw', 1, "text", "10/03/22"))
Story.commit_story(Story('22', 'fkw', 1, "text", "10/03/22"))
Story.commit_story(Story('33', 'fkw', 1, "text", "10/03/22"))
"""
print("top huggers: ", Story.top_huggers())
"""
Tree.commit_tree(Tree("1", ["12", "12"], "address", "species"))
Tree.commit_tree(Tree("2", ["12", "12"], "address", "species"))
Tree.commit_tree(Tree("3", ["12", "12"], "address", "species"))
Tree.commit_tree(Tree("4", ["12", "12"], "address", "species"))
Tree.commit_tree(Tree("5", ["12", "12"], "address", "species"))
"""
tree = Tree("1", ["12", "12"], "address", "species")
print("BEST friend: ", Story.best_friend(tree))
"""
trees_bcn.append(pro.extract_trees_bcn('data/Trees_Barcelona.json'))
trees_bcn.append(pro.extract_trees_bcn('data/Trees_Barcelona.json'))
trees_bcn.append(pro.extract_trees_bcn('data/Trees_Barcelona.json'))
trees_bcn.append(pro.extract_trees_bcn('data/Trees_Barcelona.json'))
trees_bcn.append(pro.extract_trees_bcn('data/Trees_Barcelona.json'))
trees_bcn.append(pro.extract_trees_bcn('data/Trees_Barcelona.json'))
trees_bcn.append(pro.extract_trees_bcn('data/Trees_Barcelona.json'))
trees_bcn.append(pro.extract_trees_bcn('data/Trees_Barcelona.json'))
"""

print(len(trees_bcn))
"""
trees_bcn = pro.extract_trees_bcn_stream('data/Trees_Barcelona.json')
print(len(trees_bcn))
trees_bcn.append(pro.extract_trees_bcn_stream('data/Trees_Barcelona.json'))
trees_bcn.append(pro.extract_trees_bcn_stream('data/Trees_Barcelona.json'))
trees_bcn.append(pro.extract_trees_bcn_stream('data/Trees_Barcelona.json'))
trees_bcn.append(pro.extract_trees_bcn_stream('data/Trees_Barcelona.json'))
trees_bcn.append(pro.extract_trees_bcn_stream('data/Trees_Barcelona.json'))
trees_bcn.append(pro.extract_trees_bcn_stream('data/Trees_Barcelona.json'))
trees_bcn.append(pro.extract_trees_bcn_stream('data/Trees_Barcelona.json'))
trees_bcn.append(pro.extract_trees_bcn_stream('data/Trees_Barcelona.json'))

print(len(trees_bcn))
"""
