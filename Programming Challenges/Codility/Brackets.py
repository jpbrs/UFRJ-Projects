# A string S consisting of N characters is considered to be properly nested if any of the following conditions is true:
#
# S is empty;
# S has the form "(U)" or "[U]" or "{U}" where U is a properly nested string;
# S has the form "VW" where V and W are properly nested strings.
# For example, the string "{[()()]}" is properly nested but "([)()]" is not.
#
# Write a function:
#
# def solution(S)
#
# that, given a string S consisting of N characters, returns 1 if S is properly nested and 0 otherwise.
#
# For example, given S = "{[()()]}", the function should return 1 and given S = "([)()]", the function should return 0, as explained above.
#
# Write an efficient algorithm for the following assumptions:
#
# N is an integer within the range [0..200,000];
# string S consists only of the following characters: "(", "{", "[", "]", "}" and/or ")".

def nested(left : str, right : str):
    if left == "(" and right == ")":
        return True
    elif left == "[" and right == "]":
        return True
    elif left == "{" and right == "}":
        return True
    else:
        return False


def solution(A : str):
    stack = []

    for element in A:
        if element == "(" or element == "[" or element == "{":
            stack.append(element)
        else:
            if len(stack) == 0:
                return 0
            if nested(stack.pop(), element):
                pass
            else:
                return 0

    if len(stack) != 0: # apos todos os pop() a pilha nao deve possuir mais nada
        return 0
    return 1

print(solution("{[()()]}"))
print(solution("([)()]"))