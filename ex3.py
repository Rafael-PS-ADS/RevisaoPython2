def frequencia_letras(texto):
    # Remove espaços e deixa tudo minúsculo
    texto = texto.replace(" ", "").lower()

    # Cria um dicionário vazio para guardar as contagens
    frequencia = {}

    # Percorre cada letra no texto
    for letra in texto:
        if letra in frequencia:
            frequencia[letra] += 1
        else:
            frequencia[letra] = 1

    return frequencia

# Exemplo de uso:
print(frequencia_letras("Ana"))  # Saída: {'a': 2, 'n': 1}
