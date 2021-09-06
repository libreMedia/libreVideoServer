package main

import (
	"fmt"
	"os"
)

func readStats(path string) {
	//The file has to be opened first
	f, err := os.Open(path)
	// The file descriptor (File*) has to be used to get metadata
	fi, err := f.Stat()
	// The file can be closed
	f.Close()
	if err != nil {
		fmt.Println(err)
		return
	}
	// fi is a fileInfo interface returned by Stat
	fmt.Println(fi)
}
