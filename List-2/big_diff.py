#Given an array length 1 or more of ints, return the difference between the largest
#and smallest values in the array. Note: the built-in min(v1, v2) and max(v1, v2) functions
#return the smaller or larger of two values.


big_diff([10, 3, 5, 6]) → 7
big_diff([7, 2, 10, 9]) → 8
big_diff([2, 10, 7, 2]) → 8

def big_diff(nums):
  smallest = nums[0]
  biggest = nums[0]
  for x in nums:
    if x < smallest:
      smallest = x
    if x > biggest:
      biggest = x
  return biggest - smallest
