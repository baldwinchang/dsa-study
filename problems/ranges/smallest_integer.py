def smallest_integer(nums):
    positive_numbers = set()
    minimum_number = None
    for num in nums:
        if num > 0:
            positive_numbers.add(num)
            if minimum_number is None or num < minimum_number:
                minimum_number = num

    if minimum_number != 1:
        return 1

    i = 1
    while True:
        if i not in positive_numbers:
            return i
        i += 1


assert smallest_integer([-1,2,3,4,5]) == 1
assert smallest_integer([-1,1,0,2,4,5]) == 3
