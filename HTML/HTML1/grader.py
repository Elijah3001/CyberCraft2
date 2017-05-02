#In order to solve this problem you must take the binary you find on the HTML page and convert it into text. The final answer is "keep it going"
def grade(arg, key):
  if 'keep it going' or 'keepitgoing' or 'KEEPITGOING' or 'KEEP IT GOING'in key:
    return True, "Good work!"
  else:
    return False, "Nope"
