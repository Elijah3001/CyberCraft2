def grade(arg, key):
  if 'Linus Torvalds'or'LinusTorvalds'or'LINUSTOVALDS'or'LINUS TOVALDS' in key:
    return True, "Good work!"
  else:
    return False, "Nope"
