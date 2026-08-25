from collections import deque

def num_islands(grid):
    rows,cols=len(grid),len(grid[0])
    count=0

    def bfs(r,c):
        queue=deque([r,c])
        grid[r,c]=0
        
        while queue:
            x,y=queue.popleft()
            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                nx,ny=x+dx,y+dy
                if 0<= nx <rows and 0<= ny<cols and grid[nx,ny]==1:
                    grid[nx,ny]=0
                    queue.append((nx,ny))
    for r in range (rows):
        for c in range(cols):
            if grid[r][c]==1:
                bfs(r,c)
                count+=1
    return count
grid = [
  ['1','1','0'],
  ['0','1','0'],
  ['1','0','1']
]
print("Number of islands:", num_islands(grid))
