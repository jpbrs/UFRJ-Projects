package main

import (
	"bufio"
	"encoding/base64"
	"fmt"
	"io"
	"log"
	"net"
	"os"
)

// os codigos sao muito parecidos, olhar client.go para ver uma explicacao mais completa

func main() {
	listener, err := net.Listen("tcp", "127.0.0.1:8000") // cria um servidor que espera uma conexao na porta 8000 em localhost
	if err != nil {
		log.Fatal(err)
	}
	conn, err := listener.Accept()
	for {
		if err != nil {
			log.Print(err)
			continue
		}
		go handleConn(conn) // para cada conexao cria uma thread
		see_input(conn)
	}
}

func see_input(conn net.Conn) {
	input := bufio.NewScanner(os.Stdin)

	for input.Scan() {
		texto_cifrado := base64.StdEncoding.EncodeToString([]byte(input.Text()))
		texto_cifrado += "\n"
		io.WriteString(conn, texto_cifrado)
	}

	conn.Close()
}

func handleConn(conn net.Conn) {
	who := conn.RemoteAddr().String()
	fmt.Println(who + " logou")
	welcome := "Você está conectado com " + conn.LocalAddr().String() + "\n"
	welcome_cifrado := base64.StdEncoding.EncodeToString([]byte(welcome)) + "\n"
	io.WriteString(conn, welcome_cifrado)
	input := bufio.NewScanner(conn)
	for input.Scan() {
		texto_decifrad, _ := base64.StdEncoding.DecodeString(input.Text())
		message := who + ": " + string(texto_decifrad)
		io.WriteString(os.Stdout, message)
	}
	conn.Close()
}
