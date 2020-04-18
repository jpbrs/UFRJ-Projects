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
		log.Fatal(err) // joga o erro na tela como log
		os.Exit(1) // sai do programa caso detecte erro
	}
}

func main() {

	encoded_channel := make(chan string) // Canal para as mensagens encriptadas serem enfileiradas
	decoded_channel := make(chan string) // Canal para as mensagens nao-encriptadas(vindas do teclado) serem enfileiradas

	conn, err := net.Dial("tcp", "127.0.0.1:8000") // conecta atraves de tcp ao servidor pela porta 8000
	check(err) // checa os erros da conexao
	reader := bufio.NewReader(os.Stdin) // cria um buffer de leitura para as entradas do teclado
	con_reader := bufio.NewReader(conn) // cria um buffer de leitura para os dados vindos pela conexao

	go func() { // cria uma go routine/thread para enviar as mensagens que chegam da conexao(supostamente encriptadas) para um canal responsavel por desencriptar
		for {
			text, _ := con_reader.ReadString('\n') // atribui a variavel text para cada dado antes de um enter
			encoded_channel <- text // joga o texto encriptado para o canal de textos encriptados para desencriptar
		}
	}()

	go func() {
		for text := range encoded_channel { // para cada texto que chega via canal de dados encriptados
			decoded, _ := base64.StdEncoding.DecodeString(text) // desencripta os dados
			message := conn.RemoteAddr().String() + ": " + string(decoded) + "\n" // cria a mensagem para ser mostrada no terminal com o IP de quem enviou
			io.WriteString(os.Stdout, message) // Joga para o terminal a mensagem
		}
	}()

	go func() {
		for text := range decoded_channel { // para cada texto no canal de mensagens decodificadas(que vem do teclado)
			encoded := base64.StdEncoding.EncodeToString([]byte(text)) // encrypta as mensagens
			encoded += "\n" // coloca um \n para o canal saber que a mensagem acabou
			io.WriteString(conn, encoded)
		}
	}()

	for {
		text, _ := reader.ReadString('\n') // ler  o texto que vem do teclado
		decoded_channel <- text // jogar o texto para o canal de decodificar
	}

}
