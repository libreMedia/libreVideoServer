# Lib defs
import os
import subprocess

#global defs
cwdParent = path.parent.absolute()

#func to convert given file type to mp4 for libre streaming
def convertToMp4(inputFile):
    exName = str(inputFile)
    nameLen = len(exName)
    cutName = exName[:nameLen-4]
    subprocess.run(f'ffmpeg -i "{inputFile}" -c copy "{cutName}.mp4"')

def convertWalk(walkingDir, typeToConvert):
    for root, dirs, files in os.walk(walkingDir, topdown=False):
        for name in files:
            if (name.endswith(f'.{typeToConvert}')):
                print(os.path.join(root, name))
                absPath=os.path.join(root, name)
                convertToMp4(absPath)

convertWalk(cwdParent, 'mkv')