def mergesort(items):
    if len(items) <= 1:
        return items

    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]

    left = mergesort(left)
    right = mergesort(right)

    return merge(left, right)


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1

    merged += left[left_index:]
    merged += right[right_index:]

    return merged

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    num1 = ""
    num2 = ""

    if input_list is None :
        return []

    if len(input_list) <= 2:
        return input_list

    input_list = mergesort(input_list)

    for index in range(len(input_list) - 1 , -1,  -2):
        num1 += str(input_list[index])
        if index - 1 >= 0:
            num2 += str(input_list[index - 1])

    return [int(num1), int(num2)]

    pass

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[], []])
test_function([None, []])
test_function([[1], [1]])
test_function([[1,2], [1,2]])
test_function([[1,2,3], [31,2]])
test_function([[3,1,3,3], [31,33]])
