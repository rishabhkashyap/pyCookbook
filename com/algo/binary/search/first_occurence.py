def find_first_ocurrence(arr, key):
    low = 0
    high = len(arr) - 1
    result = -1
    while (low <= high):
        mid = (low + high) // 2
        if (arr[mid] == key):
            result = mid
            high = mid - 1
        elif (arr[mid] < key):
            low = mid + 1
        else:
            high = mid - 1

    return result


if __name__ == '__main__':
    arr = [2, 5, 5, 5, 6, 6, 8, 9, 9, 9]
    result = find_first_ocurrence(arr, 5)
    print("First occurrence  of 5 =  {}".format(result))
