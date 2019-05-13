def sum_numbers(numbers=None):
    if numbers == None:
        return sum(range(1,101))
    else:
        return sum(numbers)
sum_numbers([1,2,3,4])
