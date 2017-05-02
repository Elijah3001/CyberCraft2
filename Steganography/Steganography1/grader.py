#In order to solve this problems you will need to do a few steps. First make sure PIL is installed on the device, Second save the image, Third download the code, Fourth, make sure the picture and code is on the desktop, Fifth go into the terminal and make sure you're on the desktop, Sixth type in "python hide.py -d picture.png" this will decode the hidden message within the image and return "keep it going" as your final answer. 
def grade(arg, key):
  if 'keep it going' or 'keepitgoing' or 'KEEPITGOING' or 'KEEP IT GOING' in key:
    return True, "Good work!"
  else:
    return False, "Nope"
