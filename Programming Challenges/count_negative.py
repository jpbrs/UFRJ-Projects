#Nesse problema classico temos por objetivo contar quantos numeros negativos ha na matriz
#Porem, a saca eh perceber que se tratando de linhas ordenadas na matriz, nao eh necessario percorrer
#a matriz inteira(O(N*M)) para contar quantos numeros negativos existem na matriz.

input = [[-3,-2,-1,1],[-2,2,3,4],[4,5,7,8]]


def count_negative(input : bytearray):
    sum = 0
    for i in range(0,len(input)):
        if input[i] < 0:
            sum = sum + 1
        else:
            return sum
    return sum


def main(input : bytearray):
    number = 0
    for array in input:
        number = number + count_negative(array)
    print(number)

if __name__ == '__main__':
    main(input)