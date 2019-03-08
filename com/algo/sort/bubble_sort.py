def bubble_sort(numbers):
    for i in range(len(numbers)):
        j = 0
        while (j < len(numbers) - i - 1):
            if (numbers[j] > numbers[j + 1]):
                temp = numbers[j]
                numbers[j] = numbers[j + 1]
                numbers[j + 1] = temp
            j += 1
    return numbers


if __name__ == '__main__':
    numbers = [4, 2, 5, 3, 1, 20, 7]
    print(*numbers)
    numbers = bubble_sort(numbers)
    print(*numbers)
