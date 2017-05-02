#In order to solve this problems you will need to do a few steps. First make sure PIL is installed on the device, Second save the image, Third download the code, Fourth, make sure the picture and code is on the desktop, Fifth go into the terminal and make sure you're on the desktop, Sixth type in "python hide2.py -d picture2.png" this will decode the hidden message within the image and return "01110100 01101000 01101001 01110011 00100000 01101001 01110011 00100000 01100010 01101001 01101110 01100001 01110010 01111001" you will then take that and put it into a binary to text converter and your final answer will be "this is binary".
def grade(arg, key):
  if 'this is binary'or'This is binary'or'This is Binary'or'THIS IS BINARY'or'thisisbinary'or'THISISBINARY' in key:
    return True, "Good work!"
  else:
    return False, "Nope"
