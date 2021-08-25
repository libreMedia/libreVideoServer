# Importing all necessary libraries
import cv2
import os

rootPath = '../Attack On Titan Season 1/'

def screenCap(pathy, filenamey):
    path = pathy
    fileName = filenamey
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
    
    # setting frame currently to half length
    vidCap.set(1,vidLength/2)
    # reading from frame
    ret,frame = vidCap.read()

    if ret:
        name = './screen-caps/' + str(fileName) + '.jpg'
        print ('Creating...' + name)
        # writing the extracted images
        cv2.imwrite(name, frame)
    # Release all space and windows once done
    vidCap.release()
    cv2.destroyAllWindows()

for filename in os.listdir(rootPath):
    screenCap(rootPath, filename)