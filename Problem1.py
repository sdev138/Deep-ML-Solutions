# Matrix times Vector - Easy Problem

def matrix_dot_vector(a:list[list[int|float]], b:list[int|float]) -> list[int|float]:
    c = []
    for i in a:
        if len(i) != len(b):
            # can't use matrix multiplication
            return -1
        else:
            product = 0
            for index in range(len(i)):
                product += i[index] * b[index]
            c.append(product)
    return c