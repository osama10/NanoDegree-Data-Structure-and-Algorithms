def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    if input_list is None or len(input_list) == 0:
        return []

    zero_index = 0
    two_index = len(input_list) - 1
    current_index = 0

    while current_index <= two_index:
        if input_list[current_index] == 0:
            input_list[current_index],  input_list[zero_index] = input_list[zero_index], input_list[current_index]
            current_index += 1
            zero_index +=1
        elif input_list[current_index]  ==  2:
            input_list[current_index],  input_list[two_index] = input_list[two_index], input_list[current_index]
            two_index -= 1
        else:
            current_index += 1

    return input_list

def test_function(test_case):

    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
test_function([0, 0, 0, 0, 0, 0])
test_function([1, 1, 1, 1, 1, 1])
test_function([2, 2, 2, 2, 2, 2, 2])
print(sort_012([]))  # result : []
print(sort_012(None))  # result : []


