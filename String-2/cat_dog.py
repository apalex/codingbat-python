#Return True if the string "cat" and "dog" appear the same number of times in the given string.


#cat_dog('catdog') → True
#cat_dog('catcat') → False
#cat_dog('1cat1cadodog') → True

def cat_dog(str):
  countCat = 0
  countDog = 0
  for x in range(len(str)):
    if str[x:x+3] == 'dog':
      countDog += 1
    if str[x:x+3] == 'cat':
      countCat += 1
  return countCat == countDog
