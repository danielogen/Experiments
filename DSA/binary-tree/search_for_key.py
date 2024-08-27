from node import Node
import collections

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

def search(al: dict, key: str|int) -> bool:
    stack = ['g']
    visited = []
    found = False

    while stack:
        node = stack.pop()
        if node == key:
            return True
        if node not in visited:
            visited.append(node)
            [stack[x] for x in al[node]]

    return found