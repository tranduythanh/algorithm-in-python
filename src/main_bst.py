from visualize import pprint
from bst import Tree

t = Tree()

t.insert_recursive(30)
t.insert_recursive(20)
t.insert_recursive(40)
t.insert_recursive(70)
t.insert_recursive(80)
t.insert_recursive(60)
t.insert_recursive(90)
t.insert_recursive(75)
t.insert_recursive(77)

pprint(t.root)

t = Tree()

t.insert_loop(30)
t.insert_loop(20)
t.insert_loop(40)
t.insert_loop(70)
t.insert_loop(80)
t.insert_loop(60)
t.insert_loop(90)
t.insert_loop(75)
t.insert_loop(74)
t.insert_loop(77)

pprint(t.root)

print(t.get_min())
print(t.get_max())

print(t.exist_recursive(15))
print(t.exist_loop(15))
t.insert_loop(15)
pprint(t.root)
print(t.exist_recursive(15))
print(t.exist_loop(15))

t.insert_loop(13)
t.insert_loop(12)
t.insert_loop(11)
t.insert_loop(91)
t.insert_loop(92)
t.insert_loop(93)
t.insert_loop(78)
t.insert_loop(79)
pprint(t.root)

print(t.sort_lnr_recursive())
print(t.sort_lnr_loop())
print(t.sort_nlr_recursive())
print(t.sort_lrn_recursive())

t.delete(10)
pprint(t.root)
t.delete(11)
pprint(t.root)
t.delete(93)
pprint(t.root)
t.delete(20)
pprint(t.root)
t.delete(91)
pprint(t.root)

t.delete(70)
pprint(t.root)
