def any7(nums):
    """Are any of these numbers a 7? (True/False)"""
    return f'There is a 7 in the list' if (7 in nums) else f'There is no 7 in the list'

print("should be true", any7([1, 2, 7, 4, 5]))
print("should be false", any7([1, 2, 4, 5]))

