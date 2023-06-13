# CMPT120imageManip
# Mike Kim
# March 25th, 2022

import cmpt120image
actual_img = cmpt120image.getImage("bird.png")

# 1. Swap red and green
def swapRedGreen(pixels): 
  height = len(actual_img)
  width = len(actual_img[0])
  for row in range(height):
    for col in range(width):
      img = pixels[row][col]
      red = img[0]
      img[0] = img[1]
      img[1] = red
      green = img[1]
      img[1] = img[0]
      img[1] = green
  return pixels 
     
# 2. Convert to black and white
def blackWhite(pixels):
  height = len(actual_img)
  width = len(actual_img[0])
  for row in range(height):
    for col in range(width):
      img = pixels[row][col]
      
      if img[0] + img[1] + img[2] <= (256*3)/2:
        img[0] = 0 
        img[1] = 0
        img[2] = 0
        
      else:
        img[0] = 255
        img[1] = 255
        img[2] = 255
        
  return pixels   
  
# 3. Reflect
def reflect(pixels):
  img = cmpt120image.getBlackImage(len(actual_img[0]), len(actual_img))
  height = len(actual_img)
  width = len(actual_img[0])
  # top half
  for row in range((height//2)+2):
    for col in range(width):
      img[row][col] = pixels[row][col]
      
  # bottom half (reflection)   
  for row in range(height//2):
    for col in range(width):
      img[-row][col] = pixels[row][col]
    
  return img
      
# 4. Brighten
def brighten(pixels):
  height = len(actual_img)
  width = len(actual_img[0])
  
  for row in range(height):
    for col in range(width):
      img = pixels[row][col]
      if img[0] <= 229:
        img[0] += 10
      elif img[1] <= 229:
        img[1] += 10
      elif img[2] <= 229:
        img[2] += 10
  return pixels
  
# 5. Reload image
def reload(pixels):
  cmpt120image.showImage(actual_img)