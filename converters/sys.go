package main

import (
	"fmt"
	"log"
	"os"
	"os/exec"
	"path/filepath"
)

func convertToWebM(inputFile string) {
	inputFmt := inputFile[:len(inputFile)-4]
	cmdOutput, err := exec.Command("ffmpeg", "-i", inputFile, "-c:v", "libvpx", "-b:v", "1M", "-c:a", "libvorbis", inputFmt+"CONVERTED.webm").Output()
	if err != nil {
		log.Fatal(err)
	}
	fmt.Printf("%s", cmdOutput)
}

func lazyTranscode(inputFile string) {
	inputFmt := inputFile[:len(inputFile)-4]
	cmdOutput, err := exec.Command("ffmpeg", "-i", inputFile, "-c", "copy", inputFmt+"CONVERTED.mp4").Output()
	if err != nil {
		log.Fatal(err)
	}
	fmt.Printf("%s", cmdOutput)
}

func getCwd() (p string) {
	path, err := os.Getwd()
	if err != nil {
		log.Println(err)
	}
	return path // for example /home/user+
}

func getParentDir() (p string) {
	parent := filepath.Dir(getCwd())
	return parent
}

func deleteFile(inputFile string) {
	cmdOutput, err := exec.Command("rm", inputFile).Output()
	if err != nil {
		log.Fatal(err)
	}
	fmt.Printf("%s", cmdOutput)
}

func probe(inputFile string) {
	cmdOutput, err := exec.Command("ffprobe", inputFile).Output()
	if err != nil {
		log.Fatal(err)
	}
	fmt.Printf("%s", cmdOutput)
}
