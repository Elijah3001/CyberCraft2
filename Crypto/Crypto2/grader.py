def grade(arg, key):
  if 'Cyber Defender'or'CYBER DEFENDER'or'cyber defender'or 'CYBERDEFENDER' or 'cyberdefender' in key:
    return True, "Good work!"
  else:
    return False, "Nope"
