#!/usr/bin/python3
"""pyhton script that will unlock boxes"""


def canUnlockAll(boxes):
    """This is a function which will check if can unlock all the boxes
    """

    x = [0]
    for a in x:
        for boxKey in boxes[a]:
            if boxKey not in x and boxKey < len(boxes):
                x.append(boxKey)
    if len(x) == len(boxes):
        return True
    return False