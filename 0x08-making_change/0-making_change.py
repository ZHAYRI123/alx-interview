#!/usr/bin/python3
""" Making changes """


def makeChange(c, t):
    """
	determine the fewest number of coins 
	needed to meet a given amount total

    Args:
        c ([List]): [List of Coins available]
        t ([int]): [total amount needed]
    """
    if t <= 0:
        return 0
    check = 0
    temp = 0
    c.sort(reverse=True)
    for i in c:
        while check < t:
            check += i
            temp += 1
        if check == t:
            return temp
        check -= i
        temp -= 1
    return -1
