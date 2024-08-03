def meu_gerador(numeros: list[int]):
    try:
        for numero in numeros:
            yield numero*2
    except StopIteration:
        print('deu ruim')

# for i in meu_gerador(numeros=[2,4,6]):
#     print(i)


x = meu_gerador([1,2,3,4,5])

print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))

