class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        fmask = 0
        vis = set()
        dir = [1,0,-1,0,1]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] in 'abcdef':
                    val = ord(grid[i][j]) - ord('a')
                    fmask |= 1 << val

                elif grid[i][j] == '@':
                    startx, starty = i, j

        q = [(startx, starty, 0)]
        vis.add((startx, starty, 0))
        level = 0
        while q:
            nq = []
            for x,y, mask in q:
                if mask == fmask:
                    return level
                for i in range(4):
                    nx, ny = x + dir[i], y + dir[i+1]
                    if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] != '#':
                        if grid[nx][ny] == '.' or grid[nx][ny] == '@':
                            if (nx,ny,mask) not in vis:
                                vis.add((nx,ny,mask))
                                nq.append((nx,ny,mask))
                        
                        elif grid[nx][ny] in 'abcdef':
                            nmask = mask | (1 << ord(grid[nx][ny]) - ord('a'))
                            if (nx,ny,nmask) not in vis:
                                vis.add((nx,ny,nmask))
                                nq.append((nx,ny,nmask))
                        else:
                            nmask = mask & (1 << ord(grid[nx][ny]) - ord('A'))
                            if nmask and (nx,ny,mask) not in vis:
                                vis.add((nx,ny,mask))
                                nq.append((nx,ny,mask))
            level += 1
            q = nq
        return -1
        
        
