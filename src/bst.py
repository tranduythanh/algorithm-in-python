from visualize import pprint

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def __repr__(self):
        ptr = id(self)
        ret = f'{ptr}:'
        if self.left:
            ret = f'{ret} {self.left.val}'
        else:
            ret = f'{ret} None'
        ret = f'{ret} {self.val}'
        if self.right:
            ret = f'{ret} {self.right.val}'
        else:
            ret = f'{ret} None'
        return ret

    def has_no_child(self):
        return (self.left is None) and (self.right is None)

    def has_only_left(self):
        return (self.left is not None) and (self.right is None)

    def has_only_right(self):
        return (self.left is None) and (self.right is not None)

class Tree:
    def __init__(self, root = None):
        self.root = root

    def insert_recursive(self, x):
        if self.root is None:
            self.root = Node(x)
            return
        self.__insert_recursive(self.root, x)

    def __insert_recursive(self, node, x):
        if node.val == x:
            return
        if node.val < x:
            if node.right is None:
                node.right = Node(x)
                return
            self.__insert_recursive(node.right, x)
            return
        # insert to left
        if node.left is None:
            node.left = Node(x)
        self.__insert_recursive(node.left, x)

    def insert_loop(self, x):
        if self.root is None:
            self.root = Node(x)
            return

        node = self.root
        while True:
            if node.val > x:
                if node.left:
                    node = node.left
                    continue
                node.left = Node(x)
                return
            if node.right:
                node = node.right
                continue
            node.right = Node(x)
            return

    def exist_recursive(self, x):
        return self.__exist_recursive(self.root, x)

    def __exist_recursive(self, node, x):
        if node.val == x:
            return True
        if node.val < x:
            if node.right:
                return self.__exist_recursive(node.right, x)
            return False
        if node.left:
            return self.__exist_recursive(node.left, x)
        return False

    def exist_loop(self, x):
        node = self.root
        while True:
            if not node:
                return False
            if node.val == x:
                return True
            if node.val < x:
                node = node.right
                continue
            node = node.left

    def sort_lnr_recursive(self):
        return self.__lnr_recursive(self.root)

    def __lnr_recursive(self, node, arr=[]):
        if node.left:
            self.__lnr_recursive(node.left, arr)
        arr.append(node.val)
        if node.right:
            self.__lnr_recursive(node.right, arr)
        return arr

    def sort_lnr_loop(self):
        ret = []
        node = self.root
        stack = []
        while True:
            while node:
                stack.append(node)
                node = node.left
            if len(stack) > 0:
                node = stack.pop()
                ret.append(node.val)
                node = node.right
                continue
            break
        return ret

    def sort_nlr_recursive(self):
        return self.__nlr_recursive(self.root)

    def __nlr_recursive(self, node, arr=[]):
        arr.append(node.val)
        if node.left:
            self.__nlr_recursive(node.left, arr)
        if node.right:
            self.__nlr_recursive(node.right, arr)
        return arr

    def sort_lrn_recursive(self):
        return self.__lrn_recursive(self.root)

    def __lrn_recursive(self, node, arr=[]):
        if node.left:
            self.__lrn_recursive(node.left, arr)
        if node.right:
            self.__lrn_recursive(node.right, arr)
        arr.append(node.val)
        return arr

    def get_min(self):
        node = self.root
        while node.left is not None:
            node = node.left
        return node.val

    def get_min_of_node(self, node):
        while node.left is not None:
            node = node.left
        return node.val

    def get_max(self):
        node = self.root
        while node.right is not None:
            node = node.right
        return node.val

    def delete(self, x):
        self.root = self.__delete(self.root, x)

    def __delete(self, node, x):
        if node is None:
            return None
        if node.val < x:
            node.right = self.__delete(node.right, x)
            return node
        if node.val > x:
            node.left = self.__delete(node.left, x)
            return node
        if node.val == x:
            if node.has_no_child():
                return None
            # Handle case: node has a single child
            if node.has_only_left():
                return node.left
            if node.has_only_right():
                return node.right
            # handle case: node has 2 children
            #         ____C___
            #        /         \
            #       B           E <---- delete this node
            #                 /   \
            #                D     K
            #                    /   \
            #                   I     L
            #                    \
            #                     J
            # step 1: replace E by I
            # step 2: delete I
            min_value = self.get_min_of_node(node.right)
            node.val = min_value
            node.right = self.__delete(node.right, min_value)
            return node
        return node

    def traverse(self):
        return self.__traverse(self.root, [])

    def __traverse(self, node, arr=[]):
        arr.append(node)
        if node.left:
            self.__traverse(node.left, arr)
        if node.right:
            self.__traverse(node.right, arr)
        return arr

    def cal_height(self):
        return self.__cal_height(self.root)

    def __cal_height(self, node):
        if node is None:
            return 0
        a = self.__cal_height(node.left)
        b = self.__cal_height(node.right)
        if a > b:
            return (a+1)
        return (b+1)

    def build_tree(self, arr=[]):
        for item in arr:
            self.insert_recursive(item)

    def debug(self):
        pprint(self.root)
