def is_deletion(string1, string2):
  print(string1[5:])
  if not string2:
    return True
  else:
    for i in range(len(string1)):
      if is_substring(string1[i:], string2):
        return True
  return False



def is_substring(string1, string2):

  if string2 in string1:
    return True
  else:
    return False


if __name__ == "__main__":
  string1 = input("Enter Str 1 : ")
  string2 = input("Enter Str2 : ")
  print(is_deletion(string1, string2))


  
