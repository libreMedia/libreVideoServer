# Importing all necessary libraries
import cv2
import os
path = './thots/'
fileName = "2021-05-18 01-42-16.mkv"
  
# Read the video from specified path
vidCap = cv2.VideoCapture(f'{path}{fileName}')
vidLength =  int(vidCap.get(cv2.CAP_PROP_FRAME_COUNT))

try:
      
    # creating a folder named data
    if not os.path.exists('screen-caps'):
                 os.makedirs('screen-caps')
  
# if not created then raise error
except OSError:
    print ('Error: Creating directory of data')
  
# frame
currentframe = 0
  
vidCap.set(1,vidLength/2)
    # reading from frame
ret,frame = vidCap.read()

print(vidLength)

if ret:
    # if video is still left continue creating images
    name = './screen-caps/' + str(fileName) + '.jpg'
    print ('Creating...' + name)

    # writing the extracted images
    cv2.imwrite(name, frame)

    # increasing counter so that it will
    # show how many frames are created

# Release all space and windows once done
vidCap.release()
cv2.destroyAllWindows()