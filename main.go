package main

import (
	"fmt"

	"github.com/gofiber/fiber/v2"
	"github.com/gofiber/fiber/v2/middleware/cors"
)

var allData = readDb()

func main() {

	app := fiber.New()

	app.Use(cors.New(cors.Config{
		AllowOrigins: "*",
		AllowHeaders: "Origin, Content-Type, Accept",
	}))

	app.Get("/dirList", func(c *fiber.Ctx) error {
		fmt.Print(allData)
		return c.JSON(allData)
	})

	//TODO make go to DB
	app.Static("/vids", "../", fiber.Static{
		Compress:  true,
		ByteRange: true,
		Browse:    true,
	})
	app.Static("screen-shots", "./screen-caps")

	app.Listen(":9000")
}
