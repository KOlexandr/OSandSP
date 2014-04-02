import math
import ctypes
import random
from Tools.Scripts.ftpmirror import raw_input

__author__ = 'Olexandr'


def create_array(size, min_val, max_val):
    return [random.randint(min_val, max_val) for _ in range(size)]


def get_data_for_creating_array():
    size = int(raw_input("Please, input size of array: "))
    while size < 1:
        size = int(raw_input("size should be more than 0: "))
    min_val = math.fabs(int(raw_input("Please, min value in array: ")))
    max_val = math.fabs(int(raw_input("Please, max value in array: ")))

    return size, min(min_val, max_val), max(min_val, max_val)


def main():
    size, min_val, max_val = get_data_for_creating_array()
    array = create_array(size, min_val, max_val)

    dll = ctypes.CDLL("Lab4.dll")
    array_test = (ctypes.c_int * size)()
    for i in range(size):
        array_test[i] = array[i]

    print("Original array:")
    dll.printArray(array_test, ctypes.c_int(size))
    dll.caseAndSort(array_test, ctypes.c_int(size), dll.readSortNumber())
    print("Sorted array:")
    dll.printArray(array_test, ctypes.c_int(size))

while True:
    main()