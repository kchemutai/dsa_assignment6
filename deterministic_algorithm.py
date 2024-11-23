def median_of_medians(arr, k):
    """
    Deterministic algorithm to find the kth smallest element in an array.
    Uses the Median of Medians technique to ensure O(n) worst-case time complexity.
    """

    def partition_around_pivot(pivot, nums):
        """
        Partition the array into three groups:
        - lows: elements less than the pivot
        - pivots: elements equal to the pivot
        - highs: elements greater than the pivot
        """
        lows = [x for x in nums if x < pivot]
        highs = [x for x in nums if x > pivot]
        pivots = [x for x in nums if x == pivot]
        return lows, pivots, highs

    if len(arr) <= 5:
        # Base case: When the array size is 5 or less, sort and return the kth element.
        return sorted(arr)[k - 1]

    # Step 1: Divide the array into groups of 5 elements and find the median of each group.
    medians = [sorted(arr[i:i+5])[len(arr[i:i+5]) // 2] for i in range(0, len(arr), 5)]

    # Step 2: Find the median of medians recursively.
    median_of_medians_val = median_of_medians(medians, (len(medians) + 1) // 2)

    # Step 3: Partition the array around the median of medians.
    lows, pivots, highs = partition_around_pivot(median_of_medians_val, arr)

    # Step 4: Recursively find the kth smallest element.
    if k <= len(lows):
        # If k is in the low partition, recurse into lows.
        return median_of_medians(lows, k)
    elif k <= len(lows) + len(pivots):
        # If k falls within the pivot group, return the pivot value.
        return pivots[0]
    else:
        # If k is in the high partition, recurse into highs.
        return median_of_medians(highs, k - len(lows) - len(pivots))
