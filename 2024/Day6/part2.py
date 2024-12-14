import sys
import itertools as it

grid = []
for line in sys.stdin:
    grid.append(line.strip())

h = len(grid)
w = len(grid[0])

for y,l in enumerate(grid):
    for x,c in enumerate(l):
        if c == '^':
            break
    else: continue
    break

startx,starty = x,y
dx,dy = 0,-1
turn = {
    (0,-1) : (1,0),
    (1,0) : (0,1),
    (0,1) : (-1,0),
    (-1,0) : (0,-1)
}
visited = set([(x,y)])
while 0 <= x+dx < w and 0 <= y+dy < h:
    if grid[y+dy][x+dx] == '#':
        dx,dy = turn[(dx,dy)]
    else:
        y += dy
        x += dx
        visited.add((x,y))
potential_cells = visited

old_grid = [l for l in grid]

tot = 0
for k,(j,i) in enumerate(potential_cells):
    grid = [list(l) for l in old_grid]
    grid[i][j] = '#'
    
    dx,dy = 0,-1
    x,y = startx,starty
    visited = set([(x,y,dx,dy)])
    while 0 <= x+dx < w and 0 <= y+dy < h:
        if grid[y+dy][x+dx] == '#':
            dx,dy = turn[(dx,dy)]
        else:
            y += dy
            x += dx
            if (x,y,dx,dy) in visited:
                tot += 1
                break
            visited.add((x,y,dx,dy))
print(tot)