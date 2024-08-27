from node import Node

root = Node('g')
root.insert('c')
root.insert('b')
root.insert('a')
root.insert('e')
root.insert('d')
root.insert('f')
root.insert('i')
root.insert('h')
root.insert('j')
root.insert('k')

# Inorder traversal = left, root, right
def inOrderPrint(r):
    if r is None:
        return
    inOrderPrint(r.left)
    print(r.data, end=' ')
    inOrderPrint(r.right)