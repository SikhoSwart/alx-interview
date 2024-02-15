#!/usr/bin/python3
"""Write a method that determines if all the boxes can be opened."""


def canUnlockAll(boxes):
    """
    determines if all the boxes can be opened.
    """

    keys = [0]
    for i in keys:
        for key in boxes[i]:
            if key not in keys and key < len(boxes):
                keys.append(key)
    if len(keys) == len(boxes):
        return True
    return False
