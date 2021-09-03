# Importing all necessary libraries
import cv2
from PIL import Image, ImageDraw, ImageFont
import sys
import os
from pathlib import Path
from db import insertData
# userInput = sys.argv[1]

path = Path(os.getcwd())
cwdParent = path.parent.absolute()


def screenCap(pathy, filenamey):
    path = pathy
    fileName = filenamey
    # Read the video from specified path
    vidCap = cv2.VideoCapture(os.path.join(path, fileName))

    vidLength = int(vidCap.get(cv2.CAP_PROP_FRAME_COUNT))

    try:

        # creating a folder named data
        if not os.path.exists('screen-caps'):
            os.makedirs('screen-caps')
        # setting frame currently to half length
        vidCap.set(1, vidLength/2)
        # reading from frame
        ret, frame = vidCap.read()
        if path is None:
            print(f'{path} bork bork bork bork bork borkbork bork bork'+fileName)
            return
        if ret:
            exName = str(fileName)
            nameLen = len(exName)
            cutName = exName[:nameLen-4]
            name = f'./screen-caps/{cutName}.jpg'
            print('Creating...' + cutName)
            # writing the extracted images
            font=cv2.FONT_HERSHEY_TRIPLEX
            cv2.putText(frame, cutName, (30, 256), font,
                        1, (245, 229, 52), 1, cv2.LINE_AA)
            cv2.imwrite(name, frame)

        else:
            print(f'{path} bork bork bork bork bork borkbork bork bork'+fileName)

    # if not created then raise error
    except OSError:
        print(OSError)

    # Release all space and windows once done
    vidCap.release()
    cv2.destroyAllWindows()


showsDir = os.path.join(os.getcwd(), 'showsa')


# add more ors with more vid compatibility
# or file.endswith('.avi') or file.endswith('.mkv') or file.endswith('.ogv') or file.endswith('.3gp') or file.endswith('.mov')

def vidCheck(file):
    if file.endswith('.webm') or file.endswith('.mp4'):
        return 1
    else:
        return 0


def fileWalk(shoDir):
    for root, dirs, files in os.walk(shoDir, topdown=False):
        for name in files:
            if(vidCheck(name)):
                screenCap(root, name)
                print(root)
                cutName = name[:len(name)-4]
                vidFileLoc = os.path.normpath(os.path.join(str(root), name))
                vidRoute = os.path.normpath(
                    f'{str(root)[3:]}/{name}').replace('\\', '/')
                screenShotRoute = f'/screen-shots/{cutName}.jpg'
                screenShotFileLoc = os.path.normpath(
                    os.path.join('screen-shots', cutName+'.jpg'))
                insertData(name,  vidFileLoc, screenShotFileLoc,
                           vidRoute, screenShotRoute)
                print(os.path.join(root, name))
                print('this be a file!@')
        for name in dirs:
            print(os.path.join(root, name))
            print('this be a directoryyyyyyyyyyyyyy!@')


fileWalk(cwdParent)
