'''
Problem:
    Find the length of the shortest path from the top-left to the bottom right.
    A single path may only move along 0's and can't visit the same cell more than once.
Algorithm:
    1.  The bfs() function is not recursive. Rather, it is iterative, using a double-ended queue.
    2.  It 'fans out' one layer at a time, by pushing the subsequent layer onto the right end of the queue,
        while popping off the current layer from the left end of the queue.
    3.  When the current layer is fully consumed, we increment the 'length' variable,
        in order to count how many layers we had to fan out before finding a solution.
    4.  A 'for' loop, counting the current layer is utilized inside of the 'while' loop ensuring the queue is non-empty,
        in order to achieve (3) above.
    5.  After the 'while' loop terminates, we simply return 'length', if a solution was found, else -1.
'''

from collections import deque

DEBUG = False

def bfs(grid):
    # MxN matrix
    M = len(grid)
    N = len(grid[0])
    visited = set()
    queue = deque()
    start = (0,0)
    queue.append(start)
    visited.add(start)

    length = 0
    while queue:
        # Advance to the next layer.
        length += 1
        for _ in range(len(queue)):
            # Make the next move, within the current layer.
            (r, c) = queue.popleft()
            visited.add((r,c))
            neighbors = (
                (r+1, c),
                (r-1, c),
                (r, c+1),
                (r, c-1),
            )
            for (nr, nc) in neighbors:
                # Check for invalid moves
                if (
                        nr < 0 or nc < 0 # out of bounds
                        or nr >= M or nc >= N # out of bounds
                        or (nr, nc) in visited # retraced our steps
                        or grid[nr][nc] == 1 # hit a wall
                ):
                    continue

                # Valid next move. Queue it up.
                queue.append((nr, nc))

                # Did we reach the end?
                if nr == M-1 and nc == N-1:
                    # Shortest path found!
                    return length

    # BFS exhausted: No valid path found.
    return -1

if __name__ == '__main__':
    possible = [
        [0,0,0,0],
        [1,1,0,0],
        [0,0,0,1],
        [0,1,0,0],
    ]
    impossible = [
        [0,0,0,0],
        [1,1,0,0],
        [0,0,0,1],
        [0,1,1,0],
    ]
    print(bfs(possible))
    print(bfs(impossible))
