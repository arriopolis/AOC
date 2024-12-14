import sys
import itertools as it
from math import gcd

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
    for (x1,y1),(x2,y2) in it.combinations(s,2):
        for dx,dy in [(x2-x1,y2-y1),(x1-x2,y1-y2)]:
            g = gcd(dx,dy)
            dx,dy = dx//g,dy//g
            x,y = x1,y1
            while 0 <= x < w and 0 <= y < h:
                antinodes.add((x,y))
                x += dx
                y += dy
print(len(antinodes))