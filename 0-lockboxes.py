#!/usr/bin/python3
"""
0-lockboxes.py: A module to determine if all locked boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
        boxes (list of lists): A list containing lists of keys for each box.

    Returns:
        bool: True if all boxes can be opened, else False.
    """
    if not boxes:
        return False

    n = len(boxes)
    unlocked = set([0])
    keys = [0]

    while keys:
        current_box = keys.pop()
        for key in boxes[current_box]:
            if 0 <= key < n and key not in unlocked:
                unlocked.add(key)
                keys.append(key)

    return len(unlocked) == n
