#!/usr/bin/env python3
"""
You have n number of locked boxes in front of you. Each box is numbered
sequentially from 0 to n - 1 and each box may contain keys to the other boxes.
"""


def canUnlockAll(boxes):
    """
    Returns True if all boxes can be opened, False otherwise.
    """

    visited = set([0])
    keys_found = True

    while keys_found:
        keys_found = False
        for i in range(len(boxes)):
            if i not in visited:
                continue
            keys = boxes[i]
            for key in keys:
                if 0 <= key < len(boxes) and key not in visited:
                    visited.add(key)
                    keys_found = True

    return len(visited) == len(boxes)
