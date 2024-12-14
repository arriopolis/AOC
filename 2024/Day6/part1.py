import sys

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
print(len(visited))