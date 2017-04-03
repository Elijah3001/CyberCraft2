def grade(arg, key):
  if 'this is binary'or'This is binary'or'This is Binary'or'THIS IS BINARY' in key:
    return True, "Good work!"
  else:
    return False, "Nope"
