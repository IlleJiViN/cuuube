from treelib import Tree

tree = Tree()
tree.create_node("Root", "root")  # Root 노드 추가
tree.create_node("Child 1", "child1", parent="root")
tree.create_node("Child 2", "child2", parent="root")

tree.show()
