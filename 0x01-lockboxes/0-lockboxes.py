#!/usr/bin/python3
"""Solve the Lockboxes puzzel"""


def canUnlockAll(boxes):
    """
    determines if all the boxes can be opened

    Variables nameing:
    - boxes: The boxes that i intend to open.
    - used: The keys that i already used to open boxes with.
    - key: Iteration variable to hold the key that i am currently using.
    - box: Iteration variable to denote the box i am currently searching in.
    """
    if len(boxes[0]) == 0:
        return False
    used = [0]
    for key in used:
        for box in boxes[key]:
            if (box < len(boxes)) and (box not in used):
                used.append(box)
    if len(used) == len(boxes):
        return True
    return False
