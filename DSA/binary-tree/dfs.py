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

def dfs(al):
    visited = ['g']
    stack = []

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            [stack.append(x) for x in al[node]]
    print(visited)