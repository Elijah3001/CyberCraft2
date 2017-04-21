def grade(arg, key):
  if 'anonymous' 'or' 'Anonymous' 'or' 'ANONYMOUS' in key:
    return True, "Good work!"
  else:
    return False, "Nope"
