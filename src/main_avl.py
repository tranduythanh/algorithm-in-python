from avl import AVLTree
from visualize import pprint

t = AVLTree()
nums = [9, 5, 10, 0, 6, 11, -1, 1, 2]

for num in nums:
    t.insert(num)

# Preorder Traversal
print("Preorder Traversal after insertion -")
# t.preOrder(root)
pprint(t.root)

# Delete
key = 10
t.delete(key)

# Preorder Traversal
print("Preorder Traversal after deletion -")
# t.preOrder(root)
pprint(t.root)
