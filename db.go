package main

import (
	"database/sql"

	_ "github.com/mattn/go-sqlite3"
)

type dbModel struct {
	VidName           string
	VidFileLoc        string
	ScreenShotFileLoc string
	VidRoute          string
	ScreenShotRoute   string
}

func readDb() []dbModel {
	database, _ := sql.Open("sqlite3", "./video.db")
	rows, _ := database.Query("SELECT vidName, vidFileLoc, screenShotFileLoc, vidRoute, screenShotRoute FROM videos")
	var modelArray []dbModel
	var vidName string
	var vidFileLoc string
	var screenShotFileLoc string
	var vidRoute string
	var screenShotRoute string
	for rows.Next() {
		rows.Scan(&vidName, &vidFileLoc, &screenShotFileLoc, &vidRoute, &screenShotRoute)
		modelRow := dbModel{VidName: vidName, VidFileLoc: vidFileLoc, ScreenShotFileLoc: screenShotFileLoc, VidRoute: vidRoute, ScreenShotRoute: screenShotRoute}
		modelArray = append(modelArray, modelRow)
	}
	return modelArray
}
