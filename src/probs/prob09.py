
import sys
import os

# getting the name of the directory
# where the this file is present.
current = os.path.dirname(os.path.realpath(__file__))

# Getting the parent directory name
# where the current directory is present.
parent = os.path.dirname(current)

# adding the parent directory to
# the sys.path.
sys.path.append(parent)

# now we can import the module in the parent
# directory.
from avl import AVLTree

# 9) Viết chương trình xây dựng cây nhị phân tìm kiếm có chiều cao bé nhất từ một
# dãy có thứ tự tăng của các phần tử được lưu trữ trên một danh sách liên kết.


class LLNode():
    def __init__(self, val):
        self.val = val
        self.next = None

class LL():
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, val):
        if self.head is None:
            self.head = LLNode(val)
            self.tail = self.head
            return
        self.tail.next = LLNode(val)
        self.tail = self.tail.next

    def build_ll(self, arr=[]):
        for item in arr:
            self.insert(item)


if __name__ == '__main__':
    # Build linked list of an increasing array
    ll = LL()
    ll.build_ll([i for i in range(10)])

    # Using AVLTree to build the BST with lowest height
    t =AVLTree()
    cur = ll.head
    while cur is not None:
        t.insert(cur.val)
        cur = cur.next
    t.debug()
