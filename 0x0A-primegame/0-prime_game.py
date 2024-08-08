#!/usr/bin/python3
"""
The last interview problem.
"""


def prime_numbers_upto(n):
    """
    Returns the prime numbers upto n.

    Args:
    - n: The upper limit for generating the prime numbers.
    """
    # List numbers up till n as logic values
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    # Changes number and its multiples to False
    for p in range(2, int(n ** .5) + 1):
        if is_prime[p]:
            for multiple in range(p * p, n + 1, p):
                is_prime[multiple] = False

    # Turn the list into numbers
    primes = []
    for num in range(n + 1):
        if is_prime[num]:
            primes.append(num)
    return primes


def isWinner(x, nums):
    """
    Returns the winner of the prime game turn_list by Maria and Ben.
    NO, you may not place your bets. It is not acceptable.

    Args:
    - x: Number of rounds to play.
    - nums: A list of integers with each nums[i] representing
            the ith round upper limit for the play set.
    """
    if x == 0 or not x:
        return None
    if x != len(nums):
        return None
    if not nums:
        return None

    wins_log = {"Ben": 0, "Maria": 0}
    turn_list = []

    # Stimulate the rounds
    for round_num in range(x):
        if nums[round_num] < 2:
            wins_log["Ben"] += 1
            continue
        pick_from = list(range(1, nums[round_num] + 1))
        prime_list = prime_numbers_upto(nums[round_num])

        turn_count = 0
        # Game turns simulation
        for number in prime_list:
            done = False
            # Removes the prime and all its multiples
            for pick in pick_from:
                if pick == number or pick % number == 0:
                    pick_from.remove(pick)
                    done = True
            if done:
                turn_count += 1
            if turn_count % 2 == 0:
                turn_list.append("Ben")
            else:
                turn_list.append("Maria")
        wins_log[turn_list[-1]] += 1
        turn_list.clear()

    # Determine winner by comparing win log
    if wins_log.get("Ben") == wins_log.get("Maria"):
        return None
    elif wins_log.get("Ben") > wins_log.get("Maria"):
        return "Ben"
    else:
        return "Maria"
