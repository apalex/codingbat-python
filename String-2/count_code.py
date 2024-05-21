#Return the number of times that the string "code" appears anywhere
#in the given string, except we'll accept any letter for the 'd', so "cope" and "cooe" count.


#count_code('aaacodebbb') → 1
#count_code('codexxcode') → 2
#count_code('cozexxcope') → 2

def count_code(str):
  count = 0
  for x in range(len(str)):
    if str[x:x+2] == 'co' and str[x+3:x+4] == 'e':
      count += 1
  return count
