#In order to solve this problem you must take "Jfily Klmlukly" and put it through a caesar cipher you will then get in return "Cyber Defender" as your final answer.
def grade(arg, key):
  if 'Cyber Defender'or'CYBER DEFENDER'or'cyber defender'or 'CYBERDEFENDER' or 'cyberdefender' in key:
    return True, "Good work!"
  else:
    return False, "Nope"
