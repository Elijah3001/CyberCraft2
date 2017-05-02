#In order to solve this problems you will need to do a few steps. First make sure PIL is installed on the device, Second save the image, Third download the code, Fourth, make sure the picture and code is on the desktop, Fifth go into the terminal and make sure you're on the desktop, Sixth type in "python hide3.py -d picture3.png" this will decode the hidden message within the image and return "brx irxqg wkh vhfuhw phvvdjh" you will then take that and put it into a caesar cipher and your final answer will be "you found the secret message".
def grade(arg, key):
  if 'you found the secret message'or'youfoundthesecretmessage'or'YOUFOUNDTHESECRETMESSAGE'or'YOU FOUND THE SECRET MESSAGE' in key:
    return True, "Good work!"
  else:
    return False, "Nope"
