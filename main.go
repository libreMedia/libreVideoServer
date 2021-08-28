package main

import (
	"fmt"

	"github.com/gofiber/fiber/v2"
	"github.com/gofiber/fiber/v2/middleware/cors"
)

func main() {

	allData := readDb()
	app := fiber.New()

	app.Use(cors.New(cors.Config{
		AllowOrigins: "http://localhost:3000",
		AllowHeaders: "Origin, Content-Type, Accept",
	}))

	app.Get("/dirList", func(c *fiber.Ctx) error {
		fmt.Print(allData)
		return c.JSON(allData)
	})

	//TODO make go to DB
	app.Static("/vids", "../")
	app.Static("screen-shots", "./screen-caps")

	app.Listen(":9000")
}
