with open("input/Day6.txt") as f:
    ls = f.read().strip().split("\n")

# inputFile = '''....#.....
# .........#
# ..........
# ..#.......
# .......#..
# ..........
# .#..^.....
# ........#.
# #.........
# ......#...'''

# ls = inputFile.strip().split('\n')

board = {i + 1j * j: x for i, l in enumerate(ls) for j, x in enumerate(l)}

'''Why is this useful?
The board structure allows easy navigation:
Check what’s at a position: board.get(6 + 4j).
Find all walls: {pos for pos, char in board.items() if char == '#'}.
Simulate movement: Increment/decrement the complex number to move up, down, left, or right.'''

# part 1

start = next(w for w, x in board.items() if x == '^')
walls = {w for w, x in board.items() if x == '#'}
seen = set ()

z = start
dz = -1

while z in board:
    seen.add(z)
    if z + dz in walls:
        dz *= -1j
        continue
    z += dz

print(len(seen))

# part 2
def loops(x):
    new_walls = walls | {x}
    z = start
    dz = -1
    seen = set()
    while z in board:
        if (z, dz) in seen:
            return True
        seen.add((z, dz))
        if z + dz in new_walls:
            dz *= -1j
            continue
        z += dz
    return False


print(sum(map(loops, seen)))

# asnwer:1518