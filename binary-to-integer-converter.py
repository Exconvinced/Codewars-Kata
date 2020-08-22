# Given an array of ones and zeroes, convert the equivalent binary value to an integer.


def binary_array_to_number(arr):
    arr, intgr = arr[::-1], 0
    for i in range(len(arr)):
        if arr[i] != 0: intgr += 2 ** i
    return intgr