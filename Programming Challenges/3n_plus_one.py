
# Exercise 1.6.1 of Steven Skienas' book : Programming Challenges


def operation(number : int):
    array = []
    array.append(number)
    while number != 1 :
        if (number % 2):
            number = number * 3 + 1
        else:
            number = number / 2
        array.append(number)

    return array

def main(number1 : int, number2 : int):
    if number1 < 0 or number2 < 0 or number1 > 1000000 or number2 > 1000000:
        print("Invalid number. Try a number between 1000000 and zero exclusive")
    else:
        cycle_max = 0
        for i in range(number1, number2 + 1):
            cycle_len = len(operation(i))
            if cycle_len > cycle_max:
                ciclo = operation(i)
                cycle_max = cycle_len

        print("{} {} {}".format(number1, number2, cycle_max))

if __name__ == '__main__':
    main(900,1000)
