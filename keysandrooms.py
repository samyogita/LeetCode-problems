class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        vis = set()
        def dfs(node):
            vis.add(node)
            for child in rooms[node]:
                if child not in vis:
                    dfs(child)
        
        dfs(0)

        return len(vis) == len(rooms)