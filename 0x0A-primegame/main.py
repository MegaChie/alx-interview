#!/usr/bin/python3

isWinner = __import__('0-prime_game').isWinner


print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))

print("Winner: {}".format(isWinner(3, [4, 5, 1])))

print("Winner: {}".format(isWinner(3, [5, 7, 10])))

print("Winner: {}".format(isWinner(2, [5, 10])))

print("Winner: {}".format(isWinner(3, [5, 7])))

print("Winner: {}".format(isWinner(5, [5, 7])))

print("Winner: {}".format(isWinner(0, [5, 7])))

print("Winner: {}".format(isWinner(3, [])))

print("Winner: {}".format(isWinner(5, [2, 5, 1, 4])))
