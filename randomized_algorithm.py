import random

def randomized_quickselect(arr, k):
    """
    Randomized algorithm to find the kth smallest element in an array.
    Uses random pivot selection to achieve O(n) expected time complexity.
    """

    if len(arr) == 1:
        # Base case: If the array has only one element, return it.
        return arr[0]

    # Step 1: Randomly select a pivot.
    pivot = random.choice(arr)

    # Step 2: Partition the array around the pivot.
    lows = [x for x in arr if x < pivot]
    highs = [x for x in arr if x > pivot]
    pivots = [x for x in arr if x == pivot]

    # Step 3: Recursively search in the appropriate partition.
    if k <= len(lows):
        # If k is in the low partition, recurse into lows.
        return randomized_quickselect(lows, k)
    elif k <= len(lows) + len(pivots):
        # If k falls within the pivot group, return the pivot value.
        return pivots[0]
    else:
        # If k is in the high partition, recurse into highs.
        return randomized_quickselect(highs, k - len(lows) - len(pivots))
