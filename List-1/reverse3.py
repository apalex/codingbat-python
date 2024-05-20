#Given an array of ints length 3, return a new array with
#the elements in reverse order, so {1, 2, 3} becomes {3, 2, 1}.


#reverse3([1, 2, 3]) → [3, 2, 1]
#reverse3([5, 11, 9]) → [9, 11, 5]
#reverse3([7, 0, 0]) → [0, 0, 7]

def reverse3(nums):
  newArr = [0] * len(nums)
  for x in range(len(nums)):
    newArr[x] = nums[len(nums)-x-1]
  return newArr
