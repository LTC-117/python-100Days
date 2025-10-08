count = {
    "um": 10,
    "dois": 123,
    "tres": 5
}

result: int = 0

for i in count:
    if count[i] > result:
        result = count[i]

# vai imprimir apenas as keys, não os valores, pra imprimir os valores,
# fazer 'count[result]'
print(result)
