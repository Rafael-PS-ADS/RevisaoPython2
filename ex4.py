def conta_vogais(texto):
    # Deixa tudo minúsculo para facilitar a comparação
    texto = texto.lower()

    # Define as vogais
    vogais = "aeiou"

    # Cria um contador
    contador = 0

    # Percorre cada letra do texto
    for letra in texto:
        if letra in vogais:
            contador += 1

    return contador

# Exemplo de uso:
print(conta_vogais("Python e legal"))  # Saída: 5