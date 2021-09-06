package main

import (
	"fmt"
	"log"
	"os"
	"path/filepath"
)

func deleteConverted() {
	err := filepath.Walk(getParentDir()+"/showsa",
		func(path string, info os.FileInfo, err error) error {
			if err != nil {
				return err
			}
			// DELETE
			if suffixChecker(path, "CONVERTED.mp4") {
				fmt.Print("thing")
				fmt.Println(path, "convertedddd FILE DELETED")
				deleteFile(path)
			} else {
				fmt.Print(path)
			}
			return nil
		})
	if err != nil {
		log.Println(err)
	}
}
