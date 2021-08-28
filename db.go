package main

import (
	"database/sql"
	"fmt"

	_ "github.com/mattn/go-sqlite3"
)

func readDb() {
	database, _ := sql.Open("sqlite3", "./video.db")
	rows, _ := database.Query("SELECT vidName, vidFileLoc, screenShotRoute FROM videos")
	var vidFileLoc string
	var vidName string
	var screenShotRoute string
	for rows.Next() {
		rows.Scan(&vidName, &vidFileLoc, &screenShotRoute)
		fmt.Println(vidName + ": " + vidFileLoc + " " + screenShotRoute)
	}
}
