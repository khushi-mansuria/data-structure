# Selection sort


def selection_sort(num):
    for i in range(len(num)):
        lowest_value_index = i
        for j in range(i + 1, len(num)):
            if num[j] < num[lowest_value_index]:
                lowest_value_index = j
                num[i], num[lowest_value_index] = num[lowest_value_index], num[i]
    return num


list2 = [23, 14, 66, 8, 2]
print(selection_sort(list2))


# Insertion sort

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


# main
arr = ['t', 'u', 't', 'o', 'r', 'i', 'a', 'l']
print("The sorted array is:")
print(insertionSort(arr))


# Bubble sort

def bubble_sort(num):
    swap = True
    while swap:
        swap = False
        for i in range(len(num) - 1):
            if num[i] > num[i + 1]:
                num[i], num[i + 1] = num[i + 1], num[i]
                swap = True
    return num


list = [23, 14, 66, 8, 2]
print(bubble_sort(list))
