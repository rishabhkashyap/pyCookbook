def count_sort(arr, n):
    size = n + 1
    freq = [0] * size
    result = [0]*len(arr)
    for i in range(0, (len(arr))):
        if (freq[arr[i]] is None):
            freq[arr[i]] = 1
        else:
            freq[arr[i]] += 1

    # Compute location of  elements in array
    for i in range(1, len(freq)):
        freq[i] = freq[i] + freq[i - 1]

    # Fill result array
    for i in range(0,len(arr)):
        index=freq[arr[i]]-1
        result[ index]= arr[i]
        freq[arr[i]] -= 1

    return result

if __name__ == '__main__':
    arr = [1, 4, 1, 2, 7, 5, 2]
    n = 9
    print('Before sorting')
    print(*arr)
    arr=count_sort(arr, n)
    print(*arr)

