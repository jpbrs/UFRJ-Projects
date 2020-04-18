package main

import (
	"bufio"
	"encoding/base64"
	"io"
	"log"
	"net"
	"os"
)

func check(err error) { // checa a existencia de erros e encerra o programa caso seja encontrado
	if err != nil {
		log.Fatal(err)
	}
}

func main() {

	encoded_channel := make(chan string)
	decoded_channel := make(chan string)

	conn, err := net.Dial("tcp", "127.0.0.1:8000") // conecta atraves de tcp ao servidor
	check(err)
	reader := bufio.NewReader(os.Stdin)
	con_reader := bufio.NewReader(conn)

	go func() { // cria uma thread para retornar tudo que esta sendo recebido pelo conn e
		for {
			text, _ := con_reader.ReadString('\n')
			encoded_channel <- text
		}
	}()

	go func() {
		for text := range encoded_channel {
			decoded, _ := base64.StdEncoding.DecodeString(text)
			message := conn.RemoteAddr().String() + ": " + string(decoded) + "\n"
			io.WriteString(os.Stdout, message)
		}
	}()

	go func() {
		for text := range decoded_channel {
			encoded := base64.StdEncoding.EncodeToString([]byte(text))
			encoded += "\n"
			io.WriteString(conn, encoded)
		}
	}()

	for {
		text, _ := reader.ReadString('\n')
		decoded_channel <- text
	}

}
