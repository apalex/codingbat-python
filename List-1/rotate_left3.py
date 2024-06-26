#Given an array of ints length 3, return an array with the elements
#"rotated left" so {1, 2, 3} yields {2, 3, 1}.


#rotate_left3([1, 2, 3]) → [2, 3, 1]
#rotate_left3([5, 11, 9]) → [11, 9, 5]
#rotate_left3([7, 0, 0]) → [0, 0, 7]

def rotate_left3(nums):
  newArr = [0] * len(nums)
  for x in range(len(nums)):
    newArr[x] = nums[x-2]
  return newArr
