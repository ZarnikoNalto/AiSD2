def insertion_sort(arr):
    for i in range(len(arr)):
        key = arr[i]
        j = i - 1
        while(arr[j] > key and j >= 0):
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key
    return arr


def selectionSort(array, size):
    for ind in range(size):
        min_index = ind

        for j in range(ind + 1, size):
            if array[j] < array[min_index]:
                min_index = j
        (array[ind], array[min_index]) = (array[min_index], array[ind])


def bubble_sort(array):
    n = len(array)
    for i in range(n):
        already_sorted = True
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                already_sorted = False

            if already_sorted:
                break
    return array

def merge(left, right):
    result = []
    index_left = index_right = 0
    if len(left) == 0:
        return right
    if len(right) == 0:
        return left

    while len(result) < len(left) + len(right):
        if left[index_left] <= right[index_right]:
          result.append(left[index_left])
          index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1

        if index_right == len(right):
            result += left[index_left:]
            break

        if index_left == len(left):
            result += right[index_right:]
            break

    return result

def merge_sort(array):
    if len(array) < 2:
        return array
    midpoint = len(array) // 2
    return merge(left=merge_sort(array[:midpoint]), right=merge_sort(array[midpoint:]))


# function for shell sort
def shellsort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j = j - gap
            arr[j] = temp
        gap = gap // 2


def PrintList(arr):
    for i in arr:
        print(i, end=" ")
    print("\n")




def partition(array, low, high):

    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1

def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)




num = [1, 7, 4, 1, 10, 9, -2]
size = len(num)
quickSort(num, 0, size - 1)
# print('Sorted Array in Ascending Order:')
# print(num)
# print(shellSort(num))
# print("Original List")
# PrintList(num)

# shellsort(num)
# print("Sorted List")
# PrintList(num)

selectionSort(num, size)
print('The array after sorting by selection sort is:')
print(num)
