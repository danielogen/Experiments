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

# PostOder traversal =  root, right, left
def postOrderPrint(r):
    if r is None:
        return
    print(r.data, end=' ')
    postOrderPrint(r.right)
    postOrderPrint(r.left)
