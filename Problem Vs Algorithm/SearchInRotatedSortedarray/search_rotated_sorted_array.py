
def smallest_element(input_list,low, high):
    while low < high:
        mid = low + (high - low) // 2
        if input_list[mid] > input_list[high]:
            low = mid + 1
        else:
            high = mid
    return low

def binary_search(array, target, low, high):
    if array is None or len(array) < 1:
        return None

    while low <= high:

        mid = low + int((high - low) / 2)

        if array[mid] == target:
            return mid

        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    if input_list is None or number is None or len(input_list) == 0:
        return None
    low = 0
    high = len(input_list) - 1
    pivot = smallest_element(input_list, low, high)

    if input_list[pivot] <= number <= input_list[high]:
        return binary_search(input_list, number, pivot, high)
    return binary_search(input_list,number,low,pivot - 1)





def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[4,5,6,7,0,1,2],0])
print('Pass' if rotated_array_search([], 2) is None else 'Fail')
print('Pass' if rotated_array_search([], None) is None else 'Fail')  # result None
print('Pass' if rotated_array_search(None, None) is None else 'Fail')  # result None
print('Pass' if rotated_array_search(None, 9) is None else 'Fail')  # result None
