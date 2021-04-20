def bubble_sort(collection: list) -> list:
    """Implementation of Bubble Sort.
    Returns the same collection ordered by ascending.
    """
    length = len(collection)
    for i in range(length):
        swapped = False

        for j in range(length - i - 1):
            if collection[j] > collection[j + 1]:
                temp = collection[j]
                collection[j] = collection[j + 1]
                collection[j + 1] = temp
                swapped = True

        if not swapped:
            break

    return collection
