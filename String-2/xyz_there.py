#Return True if the given string contains an appearance of "xyz" where
#the xyz is not directly preceeded by a period (.). So "xxyz" counts but
#"x.xyz" does not.


xyz_there('abcxyz') → True
xyz_there('abc.xyz') → False
xyz_there('xyz.abc') → True

def xyz_there(str):
  for x in range(len(str)):
    if str[x:x+3] == 'xyz' and str[x-1] != '.':
      return True
  return False
