def merge(first_collection: list, second_collection: list) -> list:
    """Merge two sorted collections.
    Returns one merged sorted collection.
    """
    merged_collection = []

    i, j = 0, 0
    while (i < len(first_collection)) and (j < len(second_collection)):
        if first_collection[i] <= second_collection[j]:
            merged_collection.append(first_collection[i])
            i += 1
        else:
            merged_collection.append(second_collection[j])
            j += 1

    merged_collection += first_collection[i:]
    merged_collection += second_collection[j:]

    return merged_collection

def merge_sort(collection: list) -> list:
    """Implementation of Merge Sort.
    Returns the same collection ordered by ascending.
    """
    if len(collection) <= 1:
        return collection
    else:
        middle = len(collection) // 2
        first_half = merge_sort(collection[:middle])
        second_half = merge_sort(collection[middle:])

        return merge(first_half, second_half)
