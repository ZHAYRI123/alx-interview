#!/usr/bin/python3
"""Module defining isWinner function."""

def isWinner(x, nums):
    """Function to get who has won in prime game"""
    mariaWinsCount = 0
    benWinsCount = 0

    #1: Precompute primes up to the maximum n using Sieve of Eratosthenes
    max_n = max(nums)
    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False  
    for start in range(2, int(max_n**0.5) + 1):
        if is_prime[start]:
            for multiple in range(start * start, max_n + 1, start):
                is_prime[multiple] = False

    #2: Count wins for Maria and Ben
    for n in nums:
        prime_count = sum(is_prime[2:n + 1])  
        
        # Determine the winner based on the count of primes
        if prime_count % 2 == 1:  
            mariaWinsCount += 1
        else:  
            benWinsCount += 1

    #3: Determine the overall winner
    if mariaWinsCount > benWinsCount:
        return "Winner: Maria"
    elif benWinsCount > mariaWinsCount:
        return "Winner: Ben"
    else:
        return None
