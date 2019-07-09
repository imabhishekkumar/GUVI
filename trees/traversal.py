class Node:
    def __init__(self,val):
        self.val = val
        self.left= None
        self.right= None

def printInorder(root):
    if root:
        printInorder(root.left)
        print(root.val)
        printInorder(root.right)

def printPreorder(root):
        if root:
            print(root.val)
            printPreorder(root.left)
            printPreorder(root.right)

def printPostorder(root):
        if root:
            printPostorder(root.left)
            printPostorder(root.right)
            print(root.val)
        
def main():
    root = Node(1)
    root.left = Node(11)
    root.right = Node(12)
    root.left.left = Node(111)
    root.left.right = Node(112)
    root.left.left.left= Node(1111)
    root.left.left.right= Node(1112)
    print("InOrder")
    printInorder(root)
    print("PostOrder")
    printPostorder(root)
    print("PreOrder")
    printPreorder(root)
    

if __name__== "__main__":
    main()

