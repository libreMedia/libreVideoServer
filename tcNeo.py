# Importing all necessary libraries
import cv2
import sys
import os
userInput = sys.argv[1]
print(userInput)
def screenCap(pathy, filenamey):
    path = pathy
    fileName = filenamey
    # Read the video from specified path
    vidCap = cv2.VideoCapture(os.path.join(path, fileName))

    vidLength =  int(vidCap.get(cv2.CAP_PROP_FRAME_COUNT))

    try:
        
        # creating a folder named data
        if not os.path.exists('screen-caps'):
                    os.makedirs('screen-caps')
        # setting frame currently to half length
        vidCap.set(1,vidLength/2)
        # reading from frame
        ret,frame = vidCap.read()
        if path is None:
            print(f'{path} bork bork bork bork bork borkbork bork bork'+fileName)
            return
        if ret:
            exName = str(fileName)
            nameLen = len(exName)
            cutName = exName[:nameLen-4]
            name = f'./screen-caps/{cutName}.jpg'
            print ('Creating...' + cutName)
            # writing the extracted images
            cv2.imwrite(name, frame)
        else:
            print(f'{path} bork bork bork bork bork borkbork bork bork'+fileName)

    
    # if not created then raise error
    except OSError:
        print ('Error: Creating directory of data')
    
    # Release all space and windows once done
    vidCap.release()
    cv2.destroyAllWindows()
showsDir = os.path.join(os.getcwd(), 'showsa') 

# def vidCheck(file):
#     if file.endswith('.mkv'):
#         return 1
#     elif file.endswith('.mp4'):
#         return 1
#     elif file.endswith('.MP4'):
#         return 1
#     elif file.endswith('.avi'):
#         return 1
#     elif file.endswith('.webm'):
#         return 1
#     elif file.endswith('.ogg'):
#         return 1
#     elif file.endswith('.3gp'):
#         return 1
#     elif file.endswith('.mov'):
#         return 1
#     else:
#         return 0


def vidCheck(file):
    if file.endswith('.mkv') or file.endswith('.mp4') or file.endswith('.avi') or file.endswith('.webm') or file.endswith('.ogg') or file.endswith('.3gp') or file.endswith('.mov'):
        return 1
    else:
        return 0

def fileWalk(shoDir):
    for root, dirs, files in os.walk(shoDir, topdown=False):
        for name in files:
            if(vidCheck(name)):
                screenCap(root,name)
            print(os.path.join(root, name))
            print('this be a file!@')
        for name in dirs:
            print(os.path.join(root, name))
            print('this be a directoryyyyyyyyyyyyyy!@')

fileWalk(userInput)