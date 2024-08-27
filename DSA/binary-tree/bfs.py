# uses a queue
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

d = {}
def makeList(r):
    if r is None:
        return
    d[r.data] = []
    makeList(r.left)
    if r.left:
        d[r.data].append(r.left.data)
    if r.right:
        d[r.data].append(r.right.data)
    makeList(r.right)

    return d

aList = makeList(root)

def bfs(al):
    queue = collections.deque('g')
    visited = []

    while queue:
        node = queue.popleft()
        visited.append(node)
        [queue.append(x) for x in al[node]]
    return visited

