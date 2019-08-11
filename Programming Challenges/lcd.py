#Exercise 1.6.4 of Steven Skiena's Programing Challenges Book


def construct_top(number : int, size : int):
    line = ''
    full_number = str(number)
    column_size = size + 2
    for number in full_number:
        if int(number) == 1 or int(number) == 4:
            line = line + column_size*' '
        else:
            line = line + ' ' + (column_size-2)*'-' + ' '
        line = line + ' '
    print(line)


def construct_top_board(number : int, size : int):
    full_number = str(number)
    column_size = size+2
    for i in range(0,size):
        line = ''
        for number in full_number:
            if int(number) == 5 or int(number) == 6:
                line = line + '|' + (column_size-1)*' '
            elif int(number) == 1 or int(number) == 2 or int(number) == 3 or int(number) == 7:
                line = line + (column_size-1)*' ' + '|'
            else:
                line = line + '|' + (column_size-2)*' ' + '|'
            line = line + ' '
        print(line)

def construct_middle(number : int, size : int):
    line = ''
    full_number = str(number)
    column_size = size + 2
    for number in full_number:
        if int(number) == 0 or int(number) == 1 or int(number) == 7:
            line = line + column_size*' '
        else:
            line = line + ' ' + (column_size-2)*'-' + ' '
        line = line + ' '
    print(line)

def construct_bottom_board(number : int, size : int):
    full_number = str(number)
    column_size = size + 2
    for i in range(0, size):
        line = ''
        for number in full_number:
            if int(number) == 2:
                line = line + '|' + (column_size-1)*' '
            elif int(number) == 0 or int(number) == 6 or int(number) == 8:
                line = line + '|' + (column_size - 2) * ' ' + '|'
            else:
                line = line + (column_size - 1) * ' ' + '|'
            line = line + ' '
        print(line)

def construct_bottom(number : int, size : int):
    line = ''
    full_number = str(number)
    column_size = size + 2
    for number in full_number:
        if int(number) == 4 or int(number) == 1 or int(number) == 7:
            line = line + column_size * ' '
        else:
            line = line + ' ' + (column_size-2)*'-' + ' '
        line = line + ' '
    print(line)

def input_number():
    number = int(input("Digite um numero de 0 a 99999999\n"))
    if number > 99999999 or number < 0:
        print("Invalid Value\n")
        input_number()
    else:
        return number


def input_size():
    size = int(input("Digite um tamanho de 1 a 10\n"))
    if size > 10 or size < 1:
        print("Invalid Value \n")
        input_size()
    else:
        return size

def main():

    number = input_number()
    size = input_size()


    #row_size = 2*size + 3 ---> 2 * size because it will be the boards and plus 3 because will have the top, the bottom and the middle

    construct_top(number, size)
    construct_top_board(number, size)
    construct_middle(number, size)
    construct_bottom_board(number, size)
    construct_bottom(number, size)


if __name__ == '__main__':
    main()