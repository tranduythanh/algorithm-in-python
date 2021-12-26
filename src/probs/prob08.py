
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
from bst import Node, Tree
from visualize import pprint

# 8) Cho cây nhị phân T. Viết chương trình chứa các hàm có tác dụng xác định:
#     a. Tổng số nút của cây. Số nút tối đa của cây nhị phân có chiều cao h là bao
#     nhiêu? Chứng minh điều khẳng định bằng qui nạp và kiểm nghiệm lại bằng
#     chương trình.
#     b. (*) Số nút của cây ở mức k. Số nút tối đa ở mức k của cây nhị phân là bao
#     nhiêu ? Chứng minh điều khẳng định bằng qui nạp và kiểm nghiệm lại bằng
#     chương trình.
#     c. Số nút lá.
#     d. (*) Chiều cao của cây.
#     e. Tổng giá trị trường dữ liệu(số !) trên các nút của cây.
#     f. Kiểm tra xem nó có phải là một cây nhị phân chặt(là cây nhị phân mà mỗi
# nút khác nút lá đều có đúng 2 con) hay không ?
#     g. Kiểm tra xem T có phải là cây cân bằng hoàn toàn hay không ?
#     h. Số nút có đúng 2 con khác rỗng
#     i. Số nút có đúng 1 con khác rỗng
#     j. Số nút có khóa nhỏ hơn x trên cây nhị phân hoặc cây BST
#     k. Số nút có khóa lớn hơn x trên cây nhị phân hoặc cây BST
#     l. Số nút có khóa nhỏ hơn x và lớn hơn y(y ≤ x) trên cây nhị phân hoặc cây
#     BST
#     m. Duyệt cây theo chiều rộng
#     n. Duyệt cây theo chiều sâu
#     o. Độ lệch lớn nhất của các nút trên cây(độ lệch của một nút là trị tuyệt đối
# của hiệu số giữa chiều cao của cây con phải và cây con trái của nó)
#     p. Đảo nhánh trái và phải của mọi nút trên một cây nhị phân
#     Yêu cầu: viết các thao trên bằng 2 phương pháp: đệ quy và lặp(*).


#     a. Tổng số nút của cây. Số nút tối đa của cây nhị phân có chiều cao h là bao
#     nhiêu? Chứng minh điều khẳng định bằng qui nạp và kiểm nghiệm lại bằng
#     chương trình.
def count_nodes(t):
    count = 0
    for x in t.traverse():
        count += 1
    return count

def count_leaves(t):
    count = 0
    for node in t.traverse():
        if node.has_no_child():
            count += 1
    return count

def total_value(t):
    ret = 0
    for node in t.traverse():
        ret += node.val
    return ret

def is_strict(t):
    for node in t.traverse():
        if node.has_only_left() or node.has_only_right():
            return 'không thỏa mãn'
    return 'thỏa mãn'

def max_num_nodes_of_height(h=0):
    count = 0
    for i in range(h):
        count += 2**i
    return count

def max_num_nodes_of_level(h=0):
    return 2**(h-1)

def is_perfect(t):
    h = t.cal_height()
    if max_num_nodes_of_height(h) == count_nodes(t):
        return 'thỏa mãn'
    return 'không thỏa mãn'

def count_nodes_have_2_children(t):
    count = 0
    for node in t.traverse():
        if node.left is not None and node.right is not None:
            count += 1
    return count

def count_nodes_have_1_children(t):
    count = 0
    for node in t.traverse():
        if node.has_no_child():
            continue
        if node.left is not None and node.right is not None:
            continue
        count += 1
    return count


def count_nodes_less_than(t, x):
    count = 0
    for node in t.traverse():
        if node.val < x:
            count += 1
    return count


def count_nodes_greater_than(t, x):
    count = 0
    for node in t.traverse():
        if node.val > x:
            count += 1
    return count


def count_nodes_in_range(t, y, x):
    count = 0
    for node in t.traverse():
        if node.val < x and node.val > y:
            count += 1
    return count

class QueueNode():
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Queue():
    def __init__(self, qn = None):
        self.head = qn
        self.tail = qn

    def length(self):
        if self.head is None:
            return 0
        count = 0
        while True:
            count += 1
            self.head = self.head.next
        return count

    def push(self, data):
        if self.head is None:
            self.head = QueueNode(data)
            self.tail = self.head
            return
        self.tail.next = QueueNode(data)
        self.tail = self.tail.next

    def get(self):
        if self.head is None:
            return None
        ret = self.head
        self.head = self.head.next
        return ret

def traverse_bfs(t):
    ret = []
    q = Queue(QueueNode(data=t.root))

    msg = q.get()
    while msg is not None:
        if msg.data is not None:
            # handle current data
            ret.append(msg.data)

            # check to push more msg to queue
            if msg.data.left is not None:
                q.push(msg.data.left)
            if msg.data.right is not None:
                q.push(msg.data.right)
        msg = q.get()
    return ret


def traverse_dfs(t):
    return __traverse_dfs(t.root)

def __traverse_dfs(node, arr=[]):
    arr.append(node)
    if node.left:
        __traverse_dfs(node.left, arr)
    if node.right:
        __traverse_dfs(node.right, arr)
    return arr

def traverse_dfs(t):
    return __traverse_dfs(t.root)

def __traverse_dfs(node, arr=[]):
    arr.append(node)
    if node.left:
        __traverse_dfs(node.left, arr)
    if node.right:
        __traverse_dfs(node.right, arr)
    return arr

def cal_balance_factor(t):
    bfs_arr = traverse_bfs(t)
    h = dict()
    b = dict()
    maxb = 0
    for i in range(len(bfs_arr)-1, -1, -1):
        node = bfs_arr[i]
        if node.has_no_child():
            h[node.val] = 0
            b[node.val] = 0
            continue
        if node.left is None:
            h[node.val] = h[node.right.val]+1
            b[node.val] = h[node.right.val]+1
            if b[node.val] > maxb:
                maxb = b[node.val]
            continue
        if node.right is None:
            h[node.val] = h[node.left.val]+1
            b[node.val] = h[node.left.val]+1
            if b[node.val] > maxb:
                maxb = b[node.val]
            continue
        h[node.val] = max(h[node.left.val],h[node.right.val])+1
        b[node.val] = h[node.left.val] - h[node.right.val]
        if b[node.val] < 0:
            b[node.val] = -b[node.val]
        if b[node.val] > maxb:
            maxb = b[node.val]
    print("Độ cao các nút trên cây:                       ", h)
    print("Độ lệch của các nút trên cây:                  ", b)
    print("Độ lệch lớn nhất là:                           ", maxb)

def swap_branch(node):
    if node is None:
        return
    tmp = node.right
    node.right = node.left
    node.left = tmp\

def swap_tree_recursive(t):
    __swap_tree_recursive(t.root)

def __swap_tree_recursive(node):
    swap_branch(node)
    if node.left:
        __swap_tree_recursive(node.left)
    if node.right:
        __swap_tree_recursive(node.right)


def swap_tree_loop(t):
    q = Queue(QueueNode(data=t.root))

    msg = q.get()
    while msg is not None:
        if msg.data is not None:
            # handle current data
            swap_branch(msg.data)

            # check to push more msg to queue
            if msg.data.left is not None:
                q.push(msg.data.left)
            if msg.data.right is not None:
                q.push(msg.data.right)
        msg = q.get()


if __name__ == '__main__':
    t = Tree()
    t.build_tree([10, 20, 7, 3, 23, 8, 9, 11, 15, 13, 19])
    t.debug()

    print("Tổng số nút của cây:                           ", count_nodes(t))
    h = 5
    print("Số nút tối đa của cây có độ cao h =", h,
            "là:      ", max_num_nodes_of_height(h))
    print("Số nút tối đa của cây ở tầng h =", h,
            "là:         ", max_num_nodes_of_level(h), "(h đánh chỉ số từ 0)")
    print("Số nút lá của cây ở trên là:                   ", count_leaves(t))
    print("Tổng giá trị trường dữ liệu số:                ", total_value(t))
    print("Cây có phải là cây nhị phân chặt không?        ", is_strict(t))
    print("Cây có cân bằng hoàn hảo không?                ", is_perfect(t))
    print("Số nút có đúng 2 con khác rỗng:                ",
          count_nodes_have_2_children(t))
    print("Số nút có đúng 1 con khác rỗng:                ",
          count_nodes_have_1_children(t))
    x=20
    y=10
    print("Số nút có giá trị nhỏ hơn", x, ":                 ",
          count_nodes_less_than(t, x))
    print("Số nút có giá trị lớn hơn", x, ":                 ",
          count_nodes_greater_than(t, x))
    print("Số nút có giá trị trong khoảng (",y,",",x,")","là: ",
          count_nodes_in_range(t, y, x))

    bfs_arr = traverse_bfs(t)
    print("Duyệt cây theo chiều rộng:                     ", [x.val for x in bfs_arr])
    dfs_arr = traverse_dfs(t)
    print("Duyệt cây theo chiều sâu:                      ", [x.val for x in dfs_arr])

    cal_balance_factor(t)
    print("swap tree recursively:")
    swap_tree_recursive(t)
    t.debug()

    print("swap tree again using loop:")
    swap_tree_loop(t)
    t.debug()
