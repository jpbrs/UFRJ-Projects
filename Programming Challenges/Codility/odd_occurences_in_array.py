#Dado um array [9,3,9,3,9,7,9] descobrir qual desses numeros nao possui um par
#A complexidade esperada eh O(n) e o retorno deve ser a resposta(7).

input = [9,3,9,3,9,7,9]

def main(input : bytearray):
    dict = {}

    for item in input:
        try:
            if dict[item]:
                del dict[item]

        except KeyError:
            dict[item] = item

    return list(dict.values())


if __name__ == '__main__':
    print(main(input))


