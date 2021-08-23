package main

import (
	"github.com/gofiber/fiber/v2"
	"github.com/gofiber/fiber/v2/middleware/cors"
)

func main() {

	listDirContentRoot := listDirContent("./thots")

	app := fiber.New()

	app.Use(cors.New(cors.Config{
		AllowOrigins: "http://localhost:3000",
		AllowHeaders: "Origin, Content-Type, Accept",
	}))

	app.Get("/dirList", func(c *fiber.Ctx) error {
		return c.JSON(listDirContentRoot)
	})

	app.Static("/static", "./public")

	app.Listen(":9000")
}
