from visualize import pprint

class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1

class AVLTree():
    def __init__(self, root=None):
        self.root = root

    def height_of(self, node):
        if not node:
            return 0
        return node.height

    def cal_balance(self, node):
        if not node:
            return 0
        left_height = self.height_of(node.left)
        right_height = self.height_of(node.right)
        return left_height - right_height

    def find_min_value_node(self, node):
        if node is None or node.left is None:
            return node
        return self.find_min_value_node(node.left)

    def insert(self, val):
        self.root = self.__insert(self.root, val)

    def __insert(self, node, val):
        if not node:
            return Node(val)
        elif val == node.val:
            return node
        elif val < node.val:
            node.left = self.__insert(node.left, val)
        else:
            node.right = self.__insert(node.right, val)

        node.height = 1 + max(self.height_of(node.left), self.height_of(node.right))

        balance = self.cal_balance(node)

        # Left Left
        if balance > 1 and val < node.left.val:
            return self.rotate_right(node)

        # Right Right
        if balance < -1 and val > node.right.val:
            return self.rotate_left(node)

        # Left Right
        if balance > 1 and val > node.left.val:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        # Right Left
        if balance < -1 and val < node.right.val:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    def delete(self, val):
        self.root = self.__delete(self.root, val)

    def __delete(self, node, val):
        if not node:
            return node

        elif val < node.val:
            node.left = self.__delete(node.left, val)

        elif val > node.val:
            node.right = self.__delete(node.right, val)

        else:
            if node.left is None:
                temp = node.right
                node = None
                return temp

            elif node.right is None:
                temp = node.left
                node = None
                return temp

            temp = self.find_min_value_node(node.right)
            node.val = temp.val
            node.right = self.__delete(node.right, temp.val)

        if node is None:
            return node

        node.height = 1 + max(self.height_of(node.left), self.height_of(node.right))

        balance = self.cal_balance(node)

        # Left Left
        if balance > 1 and self.cal_balance(node.left) >= 0:
            return self.rotate_right(node)

        # Right Right
        if balance < -1 and self.cal_balance(node.right) <= 0:
            return self.rotate_left(node)

        # Left Right
        if balance > 1 and self.cal_balance(node.left) < 0:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        # Right Left
        if balance < -1 and self.cal_balance(node.right) > 0:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    def rotate_left(self, y):
        z = y.right
        T2 = z.left

        z.left = y
        y.right = T2

        y.height = 1 + max(
            self.height_of(y.left),
            self.height_of(y.right)
        )
        z.height = 1 + max(
            self.height_of(z.left),
            self.height_of(z.right)
        )

        return z

    def rotate_right(self, z):
        y = z.left
        T2 = y.right

        y.right = z
        z.left = T2

        z.height = 1 + max(
            self.height_of(z.left),
            self.height_of(z.right)
        )
        y.height = 1 + max(
            self.height_of(y.left),
            self.height_of(y.right)
        )

        return y

    def build_tree(self, arr=[]):
        for item in arr:
            self.insert(item)

    def debug(self):
        pprint(self.root)
