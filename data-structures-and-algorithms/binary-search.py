# Function representing a binary search
def binarySearchFunc(arr: list[int], num: int) -> bool:
    arr.sort()
    front = 0
    back = len(arr) - 1

    # count = 0
    while front <= back:
        middle = (front + back) // 2
        # print(count)
        if num > arr[middle]:
            front = middle
        elif num < arr[middle]:
            back = middle
        elif num == arr[middle]:
            return True
        # count += 1
    return False


arr = [5, 20, 1, 74, 14, 99, -4]

# print(len(arr) - 1)
# print(3 // 2) # Do floor division with the // operator

inp = int(input('I can find the closest int to your input. Type on in to find out: '))

print(binarySearchFunc(arr, inp))
