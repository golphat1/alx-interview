#!/usr/bin/python3

def canUnlockAll(boxes):
    '''
    Function to determine if all boxes can be unlocked.
    Args:
        boxes (list of list of int):
        List of boxes containing keys to other boxes.
    Returns:
        bool: True if all boxes can be unlocked, False otherwise.
    '''

    if not isinstance(boxes, list):
        return False

    num_boxes = len(boxes)
    if num_boxes == 0:
        return False

    # Initialize a set to keep track of boxes seen and a queue to explore keys
    seen = set()
    keys_queue = [0]  # Start with the key to the first box

    while keys_queue:
        box_idx = keys_queue.pop(0)
        seen.add(box_idx)
        keys = boxes[box_idx]
        for key in keys:
            if key < num_boxes and key not in seen:
                keys_queue.append(key)

    # Check if all boxes have been seen
    return len(seen) == num_boxes
