# Exercise 1.6.3 of Steven Skienas' book : Programming Challenges

def main(input):
    number_of_students = float(input[0])
    sum = 0.0
    lista = input[1:]
    for payment in lista:
        sum = sum + payment

    mean = sum/number_of_students
    if(mean % 0.01):
        mean = round(mean,2)+0.01


    cashier = 0.0

    #Removendo a grana extra e colocando no caixa para dar para outros que possuem menos
    for i in range(len(lista)):
        if lista[i] > mean:
            cashier = cashier + lista[i] - mean
            lista[i] = mean

    max_cashier = cashier

    # Aqui adicionariamos o dinheiro extra para os que estao abaixo da media
    # for i in range(len(lista)):
    #     if lista[i] < mean:
    #         cashier = cashier - (mean-lista[i])
    #         lista[i] = mean
    # print(lista)

    print(max_cashier)


if __name__ == '__main__':
    main([4,15,15.01,3, 3.01])
