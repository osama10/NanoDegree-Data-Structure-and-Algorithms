import sys
import random

def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if ints is None or len(ints) == 0:
        return None, None

    max_num = - sys.maxsize - 1
    min_num = sys.maxsize

    for num in ints:
        if max_num < num:
            max_num = num

        if min_num > num:
            min_num = num

    return min_num, max_num


l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
print ("Pass" if ((None, None) == get_min_max(None)) else "Fail")
print ("Pass" if ((None, None) == get_min_max([])) else "Fail")
print ("Pass" if ((-341, -1) == get_min_max([-54,-2,-124,-341,-1, -341])) else "Fail")
print ("Pass" if ((-341, 2312) == get_min_max([-54,-2,-124,-341,-1, -341,2312,431,23])) else "Fail")