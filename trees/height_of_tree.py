class Node:
    def __init__(self,data):
        self.data = data
        self.left= None
        self.right= None

def maxHeight(node):
    if node is None:
        return 0
    else:
        lHeight = maxHeight(node.left)
        rHeight = maxHeight(node.right)

        if(lHeight>rHeight):
            return lHeight+1
        else:
            return rHeight+1
def main():
    root = Node(1)
    root.left = Node(11)
    root.right = Node(12)
    root.left.left = Node(111)
    root.left.right = Node(112)
    root.left.left.left= Node(1111)
    root.left.left.right= Node(1111)
    print(maxHeight(root))

if __name__== "__main__":
    main()