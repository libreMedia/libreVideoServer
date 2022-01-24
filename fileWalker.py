# Importing all necessary libraries
import cv2
import subprocess
import json
import os
from pathlib import Path
from db import insertData, insertCodec
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
            return
        if ret:
            exName = str(fileName)
            nameLen = len(exName)
            cutName = exName[:nameLen-4]
            name = f'./screen-caps/{cutName}.webp'
            print('Creating screen shot of ===> ' + cutName)
            # writing the extracted images
            font = cv2.FONT_HERSHEY_TRIPLEX
            cv2.putText(frame, 'Libre Video', (50, 50), font,
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

# dumb vid type checker
def isVideoExtension(file):
    if file.endswith('.webm') or file.endswith('.mp4') or file.endswith('.mkv') or file.endswith('.mov'):
        return 1
    else:
        return 0

#smrt vid codec checker
vidCompList = [
    'h264',
    'h263',
    'mpeg4',
    'msmpeg4v3',
    'mpeg4v3',
    'theora',
    'vp8',
    'vp9',
    'av1',

]

audCompList = [
    'mp3',
    'aac',
    'flac',
    'opus',
    'vorbis',
    'pcm',

]

def isVideoBrowserCompatible(string, videoCompatibilityList):
    if any(string in s for s in videoCompatibilityList):
        return 1
    else:
        return 0

def isAudioBrowserCompatible(string, audioCompatibilityList):
    if any(string in s for s in audioCompatibilityList):
        return 1
    else:
        return 0

def isBrowserCodecCompatible(file):
    cmd = f'ffprobe -show_format -show_streams -loglevel quiet -print_format json "{file}"'
    probe = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT);
    probeStream = json.loads(probe.decode("utf-8"))
    # print(probeStream)
    vidStream = probeStream['streams'][0]
    vidCodec = vidStream['codec_name']
    audioStream = probeStream['streams'][1]
    audioCodec = audioStream['codec_name']
    if isVideoBrowserCompatible(vidCodec, vidCompList) and isAudioBrowserCompatible(audioCodec, audCompList):
        insertCodec(vidCodec, audioCodec)
        print('BROWSER COMPATIBLE CODECS!')
        return True
    else:
        return False






def rubbishReject(fullString, substring):
    if fullString.find(substring) != -1:
        print(f"Back to the rubbish with you {fullString}!")
        # os.system(f"rm -r {fullString}")
        return 1
    else:
        print(f"You may pass...{fullString}")
        return 0

# TODO add paraam to be able to change webp/jpg/png for screenshot as jpg is faster, but quality is lower and file size seems same or higher...while 
# webp is best compression and quality, but takes longer to create the photo file
def fileWalk(shoDir):
    for root, dirs, files in os.walk(shoDir, topdown=False):
        for name in files:
            if(rubbishReject(root, ("$RECYCLE.BIN"))==0):
                if(isVideoExtension(name)):
                        if isBrowserCodecCompatible(os.path.join(str(root), name)) == True:
                            screenCap(root, name)
                            cutName = name[:len(name)-4]
                            vidFileLoc = os.path.normpath(os.path.join(str(root), name))
                            vidRoute = os.path.normpath(f'{str(root)[3:]}/{name}').replace('\\', '/')
                            screenShotRoute = f'/screen-shots/{cutName}.webp'
                            screenShotFileLoc = os.path.normpath(os.path.join('screen-shots', cutName+'.webp'))
                            insertData(name,  vidFileLoc, screenShotFileLoc,vidRoute, screenShotRoute)
                            print(os.path.join(root, name))
                            print('this be a file!@')
                        else:
                            print('audio codec not browser compatible check borked')
                else:
                    print('Not browser compatible extension')
            else:
                print('Reeeejected!')
                # return
        for name in dirs:
            print(os.path.join(root, name))
            print('this be a directoryyyyyyyyyyyyyy!@')


fileWalk(cwdParent)
