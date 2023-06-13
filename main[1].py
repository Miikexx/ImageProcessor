# Week 9 - Interactive Image Processor
# Name: Mike Kim
# Date: March 25th, 2022

import cmpt120image
import cmpt120imageManip

# getting distinct images - prevents overlapping
first_image = cmpt120image.getImage("bird.png")
second_image = cmpt120image.getImage("bird.png")
third_image = cmpt120image.getImage("bird.png")
fourth_image = cmpt120image.getImage("bird.png")
fifth_image = cmpt120image.getImage("bird.png")

# user interaction system - shows them options to choose

print("FILTERS")
print("1: Swap red and green")
print("2: Convert to black and white")
print("3: Reflect")
print("4: Brighten")
print("5: Reload Image")
print("0: Quit")

# beginning of while loop

# declaring boolean
using = True

#while loop that goes until user types 0:

while(using == True):
  
  enter_num = int(input("Enter 1 to 5, 0 to quit: "))
  # Output scenarios
  if enter_num == 0:
    print("The image processor will be quitting.")
    using = False
  
  elif enter_num == 1:
    # apply 
    first_image = cmpt120imageManip.swapRedGreen(first_image)
    # show and save image
    cmpt120image.showImage(first_image)
    cmpt120image.saveImage(first_image,"imgRGswap.png")
    
  elif enter_num == 2:
    # apply 
    second_image = cmpt120imageManip.blackWhite(second_image)
    # show and save image
    cmpt120image.showImage(second_image)
    cmpt120image.saveImage(second_image,"imgBW.png")

  elif enter_num == 3:
    # apply 
    third_image = cmpt120imageManip.reflect(third_image)
    # show and save image
    cmpt120image.showImage(third_image)
    cmpt120image.saveImage(third_image,"imgReflect.png")

  elif enter_num == 4:
    # apply 
    fourth_image = cmpt120imageManip.brighten(fourth_image)
    # show and save image
    cmpt120image.showImage(fourth_image)
    cmpt120image.saveImage(fourth_image,"imgBright.png")

  elif enter_num == 5:
    #show image without saving
    cmpt120image.showImage(fifth_image)
