# Libre Video
![Libre video logo](https://i.ibb.co/pbC7mhp/libre-Vid-Trans.png)

# Current Functionality

## The thumbnail capper
currently the functionality to walk through a given file and take a screenshot of all your files is avaible by running;
```
py tcNeo.py ../DIR_YOU_WANT_TO_WALK
```
This will walk all the directories in the given directory and find all the video files, and then take screenshots of thos video files.

## File Server
The go server will serve all files in the /public folder to /static at the hosted port.
to start the server either build the exicutible with
```
go build ./
```
or just run the server with 
```
go run ./
```
without modification, this will host all files in the given /public directory to localhost:9000/static/THE_VIDEO_FILE_NAME.VIDEO_EXTENSION