with open("tree input.txt","r")as f:
    grid = f.read().splitlines()
data = []
for i in grid:
    data.append(int(i,16))
print(data)
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
 
 
def insert(root, newValue):
    # if binary search tree is empty, make a new node and declare it as root
    if root is None:
        root = BinaryTreeNode(newValue)
        return root
    # binary search tree is not empty, so we will insert it into the tree
    # if newValue is less than value of data in root, add it to left subtree and proceed recursively
    if newValue < root.data:
        root.leftChild = insert(root.leftChild, newValue)
    else:
        # if newValue is greater than value of data in root, add it to right subtree and proceed recursively
        root.rightChild = insert(root.rightChild, newValue)
    return root
 
 
def width(root):
    if root is None:
        return 0
    max_width = -1
    current_width = 0
    Q = [root, None]
    while Q:
        node = Q.pop(0)
        if node is None:
            if max_width < current_width:
                max_width = current_width
            current_width = 0
            if not Q or Q[0] is None:
                continue
            Q.append(None)
        else:
            current_width = current_width + 1
            Q.append(node.leftChild)
            Q.append(node.rightChild)
    return max_width
tree = BinaryTreeNode(data[0])
for i in range(1,len(data)):
    tree.insert(data[0],data[i])
print(tree.width())
