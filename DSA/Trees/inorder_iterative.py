class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inorderIterative(root):
    stack = []
    while (stack or root is not None):
        if root is not None:
            stack.append(root)
            root = root.left

        else:
            root = stack.pop()
            print(root.data, end=" ")
            root = root.right


root = BinaryTree(12)
root.left = BinaryTree(6)
root.right = BinaryTree(4)
