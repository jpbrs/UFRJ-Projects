package main

import (
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
	conn, err := net.Dial("tcp", "127.0.0.1:8000") // conecta atraves de tcp ao servidor
	check(err)

	done := make(chan struct{}) // cria um canal que servirá para sinalizar que a
	go func() {                 // cria uma thread para retornar tudo que esta sendo recebido pelo conn e
		io.Copy(os.Stdout, conn) // Tudo o que estiver escrito em conn sera colocado para ser visualizado
		log.Println("done")
		done <- struct{}{} // signal the main goroutine
	}()
	io.Copy(conn, os.Stdin)
	conn.Close()
	<-done // wait for background goroutine to finish
}

func mustCopy(dst io.Writer, src io.Reader) {
	_, err := io.Copy(dst, src)
	check(err)
}
