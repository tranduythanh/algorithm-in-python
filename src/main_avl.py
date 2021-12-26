from avl import AVLTree
from visualize import pprint

t = AVLTree(verbose=True)
nums = [9, 5, 20, 0, 6, 21, -1, 1, 2, -2, -3, 25, 26, 24, 23]

for num in nums:
    t.insert(num)

# Delete
t.delete(20)
t.delete(21)
t.delete(23)
t.delete(0)
t.delete(9)
t.delete(26)
t.delete(-3)
t.delete(-1)
t.delete(5)
t.delete(1)
t.delete(-2)
t.delete(6)
t.delete(25)
t.delete(24)
t.delete(2)
