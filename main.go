package main

import (
	"encoding/json"
	"io/ioutil"
	"log"
	"net/http"

	"github.com/gin-gonic/gin"
)

type postBody struct {
	Name string `json:"name"`
	Mail string `json:"mail"`
}

func main() {
	router := gin.Default()

	router.POST("/", funcPost)

	err := router.Run("127.0.0.1:8080")
	if err != nil {
		log.Fatal("サーバー起動に失敗", err)
	}
}

// ヘッダー、ボディ、クエリ
func funcPost(c *gin.Context) {
	ct := c.Request.Header.Get("Content-Type")

	b, _ := ioutil.ReadAll(c.Request.Body)
	var param postBody
	json.Unmarshal(b, &param)

	c.JSON(http.StatusOK, gin.H{
		"content-type": ct,
		"name":         param.Name,
		"mail":         param.Mail,
	})
}

