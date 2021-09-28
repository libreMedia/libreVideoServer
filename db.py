import sqlite3
import os

cwd = os.getcwd()

# Create table

def insertData(vidName,vidFileLoc, screenShotFileLoc, vidRoute, screenShotRoute ):

    con = sqlite3.connect("video.db")
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS videos
                (vidName text, vidFileLoc text, screenShotFileLoc text, vidRoute text, screenShotRoute text )""")
    cur.execute(f'INSERT INTO videos VALUES ("{vidName}","{vidFileLoc}","{screenShotFileLoc}", "{vidRoute}" , "{screenShotRoute}")')
    con.commit()
    con.close()


def insertCodec(vidCode,audCode):

    con = sqlite3.connect("codec.db")
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS codecs
                (vidCodec text, audioCodec text)""")
    cur.execute(f'INSERT INTO codecs VALUES ("{vidCode}","{audCode}")')
    con.commit()
    con.close()