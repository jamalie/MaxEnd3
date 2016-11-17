#   Given an array of ints length 3, figure out which is larger between the first
#   and last elements in the array, and set all the other elements to be that value. Return the changed array.

#max_end3([1, 2, 3]) -> [3, 3, 3]
#max_end3([11, 5, 9]) -> [11, 11, 11]
#max_end3([2, 11, 3]) -> [3,3,3]

def max_end3(nums):
    largest = 0
    if nums[0] > nums[len(nums)-1]:
        largest = nums[0]
    else:
        largest = nums[len(nums)-1]
    for i in range(len(nums)):
        nums[i] = largest

    return nums

print max_end3([33, 2, 3])
print max_end3([11, 5, 9])
print max_end3([42, 11, 3])