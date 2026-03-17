#Forma tambem pythonica utilizando yeld pra retornar os valores de forma parcial sempre somando e mostrando o proximo valor até terminar, nao usa recursao mas achei interessante deixar documentado
#Retorna uma lista com a sequencia de fibonacci, diferente da recursao classica de fibonacci que retorna apenas o valor

def fibonacci(n):
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print(list(fibonacci(5)))