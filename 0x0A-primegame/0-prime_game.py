#!/usr/bin/python3
""" Function for Prime game"""

def isWinner(x, nums):
    """
    Determines the winner of a set of prime number removal games.

    Args:
        x (int): The number of rounds.
        nums (list of int): A list of integers where each integer n denotes
        a set of consecutive integers starting from 1 up to and including n.

    Returns:
        str: The name of the player who won the most rounds (either "Ben"
        or "Maria").
        None: If the winner cannot be determined.

    Raises:
        None.
    """
    if x <= 0 or not nums:
        return None

    max_n = max(nums)
    primes = sieve(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes_in_game = [p for p in primes if p <= n]
        if not primes_in_game:
            ben_wins += 1
            continue

        moves = 0
        while primes_in_game:
            prime = primes_in_game[0]
            multiples = range(prime, n + 1, prime)
            primes_in_game = [p for p in primes_in_game if p not in multiples]
            moves += 1

        if moves % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

def sieve(n):
    """
    Generates a list of prime numbers up to n using the Sieve of Eratosthenes.

    Args:
        n (int): The upper limit for generating prime numbers.

    Returns:
        list: A list of prime numbers up to n.
    """
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n + 1, i):
                is_prime[j] = False

    primes = [i for i in range(2, n + 1) if is_prime[i]]
    return primes
