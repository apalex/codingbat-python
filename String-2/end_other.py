#Given two strings, return True if either of the strings appears at
#the very end of the other string, ignoring upper/lower case differences
#(in other words, the computation should not be "case sensitive").
#Note: s.lower() returns the lowercase version of a string.


#end_other('Hiabc', 'abc') → True
#end_other('AbC', 'HiaBc') → True
#end_other('abc', 'abXabc') → True

def end_other(a, b):
  a = a.lower()
  b = b.lower()
  if a[len(a)-2:] == b[len(b)-2:] and len(a) > 1 and len(b) > 1:
    return True
  if a[len(a)-1:] == b[len(b)-1:] and len(a) < 2 or len(b) < 2:
    return True
  return False

#Solution
def end_other(a, b):
  a = a.lower()
  b = b.lower()
  return (b.endswith(a) or a.endswith(b))
