#Given three ints, a b c, return True if one of b or c is "close"
#(differing from a by at most 1), while the other is "far", differing
#from both other values by 2 or more. Note: abs(num) computes the absolute value of a number.


#close_far(1, 2, 10) → True
#close_far(1, 2, 3) → False
#close_far(4, 1, 3) → True

def close_far(a, b, c):
  lenAB = abs(a-b)
  lenAC = abs(a-c)
  lenBC = abs(b-c)
  if lenAB <= 1 and lenAC >= 2 and lenBC >= 2 or lenAC <= 1 and lenBC >= 2 and lenAB >= 2:
    return True
  return False
