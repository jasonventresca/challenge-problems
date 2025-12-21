import json

'''
problem:
    count the unique paths from the top left to the bottom right
    a single path may only move along 0's and can't visit the same cell more than once.
algorithm:
    move_to(r, c, visited) takes the desired position to move to and an existing visited set.
    call move_to(0,0).
    it calls move_to() for each neighboring cell not already in visited
    increment a counter for every call to move_to(end,end)
'''

matrix = [
    [0,0,0,0],
    [1,1,0,0],
    [0,0,0,1],
    [0,1,0,0],
]
unique_paths = 0
# MxN matrix
M = len(matrix)
N = len(matrix[0])

DEBUG = False
def move_to(r: int, c: int, visited, path) -> None:
    global unique_paths
    if DEBUG: print(f'move_to({r}, {c}, {visited})')
    # invalid: out of bounds
    if r < 0 or r >= M or c < 0 or c >= N:
        return
    # invalid: hit a wall
    if matrix[r][c] == 1:
        return
    # invalid: we've retraced our steps
    if (r,c) in visited:
        return
    
    # mark visited, track path
    visited.add((r,c))
    path.append((r,c))
    
    # solution: found a valid, unique path to the end
    if r == M-1 and c == N-1:
        print(f'found a unique path:')
        print(f'{json.dumps(path, indent=4)}')
        unique_paths += 1
        return
    
    # try the 4 cardinal directions
    # left
    move_to(r-1, c, set(visited), path)
    # right
    move_to(r+1, c, set(visited), path)
    # up
    move_to(r, c-1, set(visited), path)
    # down
    move_to(r, c+1, set(visited), path)
    
    path.pop()
    visited.remove((r,c))


start = (0, 0)
move_to(0, 1, set((start,)), [start,])
print(unique_paths)
