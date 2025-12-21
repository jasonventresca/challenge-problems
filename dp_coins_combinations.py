#!/usr/bin/env python3

from typing import List
import json

DEBUG = False

def solution(coins: List[int], amount: int) -> int:
    '''
    This problem can be approached with DP, by building up from smaller to larger amounts.
    Since order does not matter, we need to avoid double counting coin combinations
    that are actually just permutations of the same combination.
    The second dimension is going to be the amount we're trying to make (building up from zero).
    If we make the first dimension which coins we're allowed to use, that deduplicates order by
    forcing us to use the coins in (descending) order, as we iteratively build up through the first dimension.

    So, the 2D-DP looks like this:
    dp[i][a] = number of ways to make amount `a` using coins i..last coin

    Base cases:
    - amount: 0 (always possible, in exactly one way: use no coins)
    - using coins: [] i.e. no coins to choose from

    dp[x][0] = 1
    dp[0][1,2,...] = 0, i.e. there are no ways to make nonzero amounts from zero types of coins

    d[i][a] = (
        dp[i+1][a - coins[i]] + # use the coin
        dp[i+1][a]              # skip the coin
    ) if coins[i] <= a, else:
    (
        dp[i+1][a]              # skip the coin
    )
    '''
    # Initialize 2D-DP array
    nc = len(coins) + 1
    n_amts = amount + 1
    dp = [[0] * (nc) for _ in range(n_amts)]
    print(f'dp: {json.dumps(dp, indent=4)}')
    # Initialize base cases
    for i in range(nc):
        dp[i][0] = 1
    #for a in range(1, n_amts):
    #    dp[0][a] = 0
    for i in range(nc):
        for a in range(1, n_amts):
            print(f'i: {i}\ta:{a}')
            if coins[i] <= a:
                # Use the coin
                dp[i][a] = (
                    dp[i+1][a - coins[i]] + \
                    dp[i+1][a]
                )
            else:
                # Skip the coin
                dp[i][a] = dp[i+1][a]
    return dp[nc-1][n_amts-1]

def main():
    test_data = [
        { 'coins': [1,2], 'amount': 3, 'answer': 2 },
    ]

    for td in test_data:
        obs = solution(td['coins'], td['amount'])
        exp = td['answer']
        assert exp == obs, \
            f'Expected: {exp} != Observed: {obs}'

if __name__ == '__main__':
    main()
