def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number is None or number < 2:
        return number
    
    low = 0
    high = number

    while low <= high:

        mid = low + int((high - low)/2)

        if mid * mid == number or (mid * mid) < number < ((mid +1) * (mid +1)):
            return mid
        elif mid * mid < number:
            low = mid + 1
        else:
            high = mid - 1

    return low


print ("Pass" if (3 == sqrt(9)) else "Fail")
print ("Pass" if (0 == sqrt(0)) else "Fail")
print ("Pass" if (4 == sqrt(16)) else "Fail")
print ("Pass" if (1 == sqrt(1)) else "Fail")
print ("Pass" if (5 == sqrt(27)) else "Fail")
print ("Pass" if (6 == sqrt(40)) else "Fail")
print ("Pass" if (None == sqrt(None)) else "Fail")
print ("Pass" if (100 == sqrt(10200)) else "Fail")