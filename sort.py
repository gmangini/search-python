"""
Project 2 Sorting
CS 2420

Gino Mangini
"""

from random import sample, seed
from time import perf_counter
from recursioncounter import RecursionCounter


def mergesort(lyst):

    """mergesort algorithm."""

    RecursionCounter()
    for i in lyst:
        if not type(i) is int:
            raise ValueError("Only integers are allowed")

    if len(lyst) > 1:
        mid_index = len(lyst) // 2
        L = lyst[:mid_index]
        R = lyst[mid_index:]

        mergesort(L)
        mergesort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                lyst[k] = L[i]
                i += 1
            else:
                lyst[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            lyst[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            lyst[k] = R[j]
            j += 1
            k += 1
    return lyst


def selection_sort(lyst):

    """selection sort alogrithm."""

    for i in lyst:
        if not type(i) is int:
            raise ValueError("Only integers are allowed")

    for i in range(len(lyst)):
        min = i
        for j in range(i + 1, len(lyst)):
            if lyst[min] > lyst[j]:
                min = j
        lyst[i], lyst[min] = lyst[min], lyst[i]
    return lyst


def insertion_sort(lyst):

    """Insertion sort algorithm."""

    for i in lyst:
        if not type(i) is int:
            raise ValueError("Only integers are allowed")

    for i in range(1, len(lyst)):
        key = lyst[i]
        j = i - 1
        while j >= 0 and key < lyst[j]:
            lyst[j + 1] = lyst[j]
            j -= 1
        lyst[j + 1] = key
    return lyst


def quicksort(lyst):

    """quicksort algorithm"""

    RecursionCounter()

    for i in lyst:
        if not type(i) is int:
            raise ValueError("Only integers are allowed")

    if len(lyst) <= 1:
        return lyst
    else:
        return quicksort([x for x in lyst[1:] if x < lyst[0]]) + \
               [lyst[0]] + \
               quicksort([x for x in lyst[1:] if x >= lyst[0]])


def is_sorted(lyst):

    """function determines if list is sorted"""

    for i in lyst:
        if not type(i) is int:
            raise ValueError("Only integers are allowed")

    lyst1 = lyst.copy()
    if lyst == sorted(lyst1):
        return True
    else:
        return False


def timsort(lyst):

    """built in sorting function"""

    return sorted(lyst)


def main():

    """main function"""

    data_size = 1000
    seed(42)
    data = sample(range(data_size * 3), k=data_size)
    functions = [mergesort, selection_sort, quicksort, insertion_sort, timsort]
    str_func = ["mergesrt", "select_srt", "quicksrt", "insert_srt", "timsrt"]

    for i in range(len(functions)):
        lyst = data.copy()
        print("starting " + str_func[i])
        t_1 = perf_counter()
        lyst = functions[i](lyst)
        t_2 = perf_counter()
        print(str_func[i] + " duration: " + str(t_2 - t_1) + " seconds.")


if __name__ == "__main__":
    main()
