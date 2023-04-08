"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        mp = defaultdict(Node)
        q = deque([node])
        while q:
            cur = q.popleft()
            ptr = mp[cur]
            ptr.val = cur.val
            for x in cur.neighbors:
                if x in mp:
                    ptr.neighbors.append(mp[x])
                else:
                    q.append(x)
                    mp[x] = Node(x.val)
                    ptr.neighbors.append(mp[x])
        return mp[node]

                
