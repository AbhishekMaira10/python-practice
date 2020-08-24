import queue


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def buildTree(preorder, inorder):
    preLength = len(preorder)
    inLength = len(inorder)
    if preLength != inLength or preorder is None or inorder is None or preLength == 0:
        return None
    root = BinaryTreeNode(preorder[0])

    return root


def printLevelWise(root):
    if root is None:
        return
    intputQ = queue.Queue()
    outputQ = queue.Queue()


def main():
    preorder = [int(i) for i in input().strip().split()]
    inorder = [int(i) for i in input().strip().split()]
    root = buildTree(preorder, inorder)
    printLevelWise(root)


if __name__ == "__main__":
    main()
