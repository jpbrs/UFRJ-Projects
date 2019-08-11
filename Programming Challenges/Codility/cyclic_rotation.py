#Dado um vetor qualquer fazer o deslocamento de n posicoes a direita
#Exemplo : Dado um vetor [3,8,9,7,6] com input de n=2 posicoes, retornar o vetor [7,6,3,8,9]

input = [3,8,9,7,6]

def main(input : bytearray, times : int):
    total = len(input)
    new_array = input[0:]

    for i in range(0,total):
        new_index = ( i + times ) % total
        new_array[new_index] = input[i]

    return new_array

if __name__ == '__main__':
    print(main(input, 2))