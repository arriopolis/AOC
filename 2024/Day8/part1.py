import sys
import itertools as it

grid = []
for line in sys.stdin:
    grid.append(line.strip())

h = len(grid)
w = len(grid[0])

antennas = {}
for y,l in enumerate(grid):
    for x,c in enumerate(l):
        if c == '.': continue
        if c not in antennas: antennas[c] = set()
        antennas[c].add((x,y))
    
antinodes = set()
for s in antennas.values():
    for (x1,y1),(x2,y2) in it.combinations(s, 2):
        if 0 <= 2*x1-x2 < w and 0 <= 2*y1-y2 < h:
            antinodes.add((2*x1-x2, 2*y1-y2))
        if 0 <= 2*x2-x1 < w and 0 <= 2*y2-y1 < h:
            antinodes.add((2*x2-x1, 2*y2-y1))
print(len(antinodes))