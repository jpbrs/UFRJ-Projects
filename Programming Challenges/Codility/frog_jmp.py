def solution(X, Y, D):
    distance = Y-X
    resto = distance%D
    pulos = int(distance/D)
    if resto:
        return pulos+1
    else:
        return pulos

print(solution(10,85,30))
