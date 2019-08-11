# A string S consisting of N characters is called properly nested if:
#
# S is empty;
# S has the form "(U)" where U is a properly nested string;
# S has the form "VW" where V and W are properly nested strings.
# For example, string "(()(())())" is properly nested but string "())" isn't.
#
# Write a function:
#
# def solution(S)
#
# that, given a string S consisting of N characters, returns 1 if string S is properly nested and 0 otherwise.
#
# For example, given S = "(()(())())", the function should return 1 and given S = "())", the function should return 0, as explained above.
#
# Write an efficient algorithm for the following assumptions:
#
# N is an integer within the range [0..1,000,000];
# string S consists only of the characters "(" and/or ")".

def nested(left : str, right : str):
    if left == "(" and right == ")":
        return True
    else:
        return False

def solution(A : str):
    stack = []
    for element in A:
        if element == "(":
            stack.append(element)
        else:
            if len(stack) ==0:
                return 0
            elif(nested(stack.pop(), element)):
                pass
            else:
                return 0

    if len(stack)!=0:
        return 0
    return 1

print(solution("(()(())())"))
print(solution("())"))