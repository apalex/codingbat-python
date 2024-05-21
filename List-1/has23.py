#Given an int array length 2, return True if it contains a 2 or a 3.


#has23([2, 5]) → True
#has23([4, 3]) → True
#has23([4, 5]) → False

def has23(nums):
  for x in nums:
    if x is 2 or x is 3:
      return True
  return False
