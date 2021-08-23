package main

import (
	"io/ioutil"
	"log"
)

func listDirContent(dir string) []string {
	var dirList []string
	files, err := ioutil.ReadDir(dir)
	if err != nil {
		log.Fatal(err)
	}

	for _, file := range files {
		dirList = append(dirList, file.Name())
	}
	return dirList
}
