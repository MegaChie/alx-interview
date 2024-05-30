
#!/usr/bin/python3
"""Define A function to generate Pascal's Triangle"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal’s triangle of n

    Variables naming:
        - res: Short for result, and will hold
               the elements of the Pascal's Triangle.
        - n: The numbers of rows from Pascal's Triangle.
        - num: Short for number, iteration variable used to hold
               the current row we are calculating.
        - row: Represents the row final value from the triangle.
        - elem: Short for element, iteration variable holding
                the number of propabilities for the current raw.
    """
    if n <= 0:
        return []
    elif n == 1:
        return [[1]]
    elif n == 2:
        return [[1], [1, 1]]
    else:
        base = [[1], [1, 1]]
        for row in range(2, n):
            temp = [1, 1]
            for elem in range(len(base[-1]) - 1):
                a = base[-1][elem]
                b = base[-1][elem + 1]
                temp.insert(-1, a + b)
            base.append(temp)
        return base

