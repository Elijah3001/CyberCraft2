def grade(arg, key):
  if 'you found the secret message' in key:
    return True, "Good work!"
  else:
    return False, "Nope"


