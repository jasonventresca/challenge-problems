#!/usr/bin/env python3

'''
Intuition:
1.  The board is always painted with the following:
a.  The snake's body, from head to tail.
b.  The current piece of food.
2.  Separately, a double ended queue is kept for the snake's (x,y) coordinates:
a.  The queue's head is the snake's head, and
b.  the queue's tail is the snake's tail.

Algorithm:
1.  Initialize the grid as a 2D array with all positions set to 'e' (empty).
2.  Put the snake 's' at 0,0 and paint the first piece of food 'f' by removing it from the head of the list (popleft).
3.  move() does the following:
4.  Check for special cases:
a.  Check for OOB.
b.  Check for snake eating itself.
c.  Check for snake eating food.
d.  Snake moved to an empty space (assert).
5.  Repaint board:
a.  Advance snake's head (pop off tail, insert at head).
b.  Paint next food.
c.  Increase score (if ate food, above).
6.  Update deques (snake + food).
7.  Return score, or end game (above).
'''
DEBUG = False
class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        # Set up empty board
        self.width = width
        self.height = height
        self.board = [(['e'] * width) for _ in range(height)]
        assert len(self.board) == height
        assert len(self.board[0]) == width

        # Snake always starts at top-left corner.
        self.board[0][0] = 's'

        # Initialize snake and food double-ended queues for quick access.
        self.snake = deque([(0,0)])
        self.food = deque(food)

        # Place first piece of food.
        x, y = self.food.popleft()
        self.board[x][y] = 'f'
        self.render()

        # Initialize the score to zero.
        self.score = 0

    def render(self):
        if not DEBUG:
            return
        for r in range(self.height):
            print(''.join(self.board[r]))
        print('-' * self.width)

    def move(self, direction: str) -> int:
        # Get the snake's head position, before the move.
        hx, hy = self.snake[0]
        if direction == 'U':
            hx -= 1
        elif direction == 'D':
            hx += 1
        elif direction == 'R':
            hy += 1
        elif direction == 'L':
            hy -= 1
        # a.  Check for OOB.
        if min(hx, hy) < 0 or hx >= self.height or hy >= self.width :
            return -1 # Snake went out of bounds.
        # b.  Check for snake eating itself.
        # 5.  Repaint board:
        # c.  Check for snake eating food.
        if self.board[hx][hy] == 'f':
            self.score += 1
            # b.  Paint next food.
            if DEBUG: print('next food')
            if self.food:
                fx, fy = self.food.popleft()
                self.board[fx][fy] = 'f'
            # Don't pop off the tail, since the snake grew larger.
        else:
            # a.  Advance snake's head (pop off tail, insert at head).
            tx, ty = self.snake.pop()
            self.board[tx][ty] = 'e'

        if self.board[hx][hy] == 's':
            return -1 # Snake ate itself
        self.snake.appendleft((hx, hy))
        self.board[hx][hy] = 's'
        self.render()
        return self.score
        


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
