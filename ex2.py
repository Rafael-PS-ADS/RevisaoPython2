numeros = [5, 8, 13, -5, -3]

positivos = [num for num in numeros if num > 0]
if positivos:
    soma = sum(positivos)
    print("A soma dos números positivos é:", soma)
