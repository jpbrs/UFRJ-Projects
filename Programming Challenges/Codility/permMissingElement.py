#Dado um vetor que eh uma permutacao dos valores de 1 ate N precisa-se descobrir o numero que falta
# EX : A = [2,3,5,1] o retorno deve ser 4


input = [1,3,5,7,9,8,6,4,2] # deve retornar 8


def main(input : bytearray):
    tamanho = len(input)
    true_sum = (1+(tamanho+1))*((tamanho+1)/2)
    total_sum = 0
    for i in range(0,tamanho):
        total_sum = total_sum + input[i]
    return true_sum - total_sum



if __name__ == '__main__':
    print(main(input))

