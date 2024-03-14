#!/usr/bin/python3
"""Prime game module.
"""


def isWinner(v, nums):
    """Determines the winner of the game.
    """
    if v < 1 or not nums:
        return None
    marias_wins, bens_wins = 0, 0
    # primes with a limit
    n = max(nums)
    primes = [True for _ in range(1, n + 1, 1)]
    primes[0] = False
    for a, is_prime in enumerate(primes, 1):
        if a == 1 or not is_prime:
            continue
        for j in range(a + a, n + 1, a):
            primes[j - 1] = False
    # number of primes less than  nums
    for _, n in zip(range(v), nums):
        primes_count = len(list(filter(lambda v: v, primes[0: n])))
        bens_wins += primes_count % 2 == 0
        marias_wins += primes_count % 2 == 1
    if marias_wins == bens_wins:
        return None
    return 'Maria' if marias_wins > bens_wins else 'Ben'
