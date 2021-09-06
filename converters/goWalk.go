package main

import (
	"fmt"
	"log"
	"os"
	"path/filepath"
)

func main() {
	err := filepath.Walk(getParentDir()+"/showsa",
		func(path string, info os.FileInfo, err error) error {
			if err != nil {
				return err
			}
			if suffixChecker(path, ".avi") {
				fmt.Println(path, "avii file convertedddd to webmm")
				convertToWebM(path)
			} else if suffixChecker(path, ".mkv") {
				fmt.Println(path, "mkv file convertedddd to webmm")
				convertToWebM(path)
			} else {
				fmt.Println("things")
			}

			return nil
		})
	if err != nil {
		log.Println(err)
	}
}

// func main() {
// 	deleteConverted()
// }
