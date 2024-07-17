with open("tree input.txt","r")as f:
    grid = f.read().splitlines()
data = []
for i in grid:
    data.append(int(i,16))
print(data)
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(key, self.root)

    def _insert(self, key, node):
        if key < node.val:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(key, node.left)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(key, node.right)

    def getmaxwidth(self):
        if self.root is None:
            return 0
        max_width = 0
        queue = [self.root]
        while queue:
            level_size = len(queue)
            max_width = max(max_width, level_size)
            for i in range(level_size):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return max_width

    def getheight(self):
        if self.root is None:
            return 0
        return self._getheight(self.root)

    def _getheight(self, node):
        if node is None:
            return 0
        left_height = self._getheight(node.left)
        right_height = self._getheight(node.right)
        return max(left_height, right_height) + 1

node = Node(data[0])
tree = BinarySearchTree()
for i in range(1,len(data)):
    tree.insert(i)
print(tree.getmaxwidth())
print(tree.getheight())
print(int(tree.getmaxwidth())*int(tree.getheight()))