def grade(arg, key):
  if 'flag = Lawrence Livermore National Laboratory ' in key:
    return True, "Good work!"
  else:
    return False, "Nope"
