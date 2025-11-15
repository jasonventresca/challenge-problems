#!/usr/bin/env python3
# Demonstrates recursion and memoization from 1D Dynamic Programming
# This specific exercise was taken from the following video:
#   -> https://www.youtube.com/watch?v=vYquumk4nWw

def fib(n: int, memo: dict) -> int:
    cached = memo.get(n)
    if cached:
        return cached

    if n in (1, 2):
        return 1

    res = fib(n-2, memo) + fib(n-1, memo)
    memo[n] = res
    return res

def main():
    cache = {}
    for i in range(1, 11):
        print(fib(i, cache))

if __name__ == '__main__':
    main()
