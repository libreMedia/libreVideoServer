# Libre Video
<img src="https://i.ibb.co/pbC7mhp/libre-Vid-Trans.png" width="50%" height="50%" />

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
without modification, this will host all files in the given /public directory to localhost:9000/static/THE_VIDEO_FILE_NAME.VIDEO_EXTENSION

# Example Site
This is the site running on my local file server serving video files.

<img src="https://i.ibb.co/fVgK1hr/2021-08-29-07h23-43.png" width="100%" height="50%" />