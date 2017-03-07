def grade(arg, key):
  if 'anonymous' in key:
    return True, "Good work!"
  else:
    return False, "Nope"


