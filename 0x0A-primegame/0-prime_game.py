#!/usr/bin/python3
"""Module defining isWinner function."""

def isWinner(x, nums):
    """Function to determine the winner of the prime game."""
    mariaWinsCount = 0
    benWinsCount = 0

    max_n = max(nums)
    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False  
    for start in range(2, int(max_n**0.5) + 1):
        if is_prime[start]:
            for multiple in range(start * start, max_n + 1, start):
                is_prime[multiple] = False

    for n in nums:
        prime_count = sum(is_prime[2:n + 1])
        
        if prime_count % 2 == 1:
            mariaWinsCount += 1
        else:  
            benWinsCount += 1

    if mariaWinsCount > benWinsCount:
        return "Maria"
    elif benWinsCount > mariaWinsCount:
        return "Ben"
    else:
        return None
