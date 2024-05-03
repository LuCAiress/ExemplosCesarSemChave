# Nome: Lucas Lima Aires

def decifrar_com_pesos(texto_cifrado):
    ALFABETO = 'abcdefghijklmnopqrstuvwxyz'
    texto_cifrado = texto_cifrado.lower()
    # Ordem das letras mais frequentes (Decrescente)
    #letras_frequentes = ['a', 'e', 'o', 's', 'r', 'i', 'n', 'd', 'm', 'u', 't', 'c', 'l', 'p', 'v', 'g', 'h', 'q', 'b', 'f', 'z', 'j', 'x', 'k', 'w', 'y']

    # Definindo pesos com base na frequência das letras do português
    peso_letras = {'a': 14, 'e': 12, 'o': 10, 's': 8, 'r': 6, 'i': 6, 'n': 5, 'd': 4, 'm': 4, 'u': 4, 't': 4, 'c': 3, 'l': 3, 'p': 3, 'h': 2, 'q': 2, 'b': 2, 'f': 2, 'z': 1, 'j': 1, 'x': 1, 'k': 1, 'w': 1, 'y': 1}

    frequencias_chaves = []

    for chave in range(len(ALFABETO)):
        texto_decifrado = ''
        for letra in texto_cifrado:
            if letra in ALFABETO:
                indice = (ALFABETO.find(letra) - chave) % len(ALFABETO)
                texto_decifrado += ALFABETO[indice]
            else:
                texto_decifrado += letra

        # Cálculo o peso das letras mais comuns
        frequencia = {}
        for letra in texto_decifrado:
            if letra in ALFABETO:
                frequencia[letra] = frequencia.get(letra, 0) + peso_letras.get(letra, 1)

        # Calcula a frequência total dos pesos
        frequencia_total = sum(frequencia.values())

        # Armazena a frequência e a chave
        frequencias_chaves.append((frequencia_total, chave))

    # Ordena a lista nas top 3 maiores frequências com peso (Decrescente)
    frequencias_chaves.sort(reverse=True)
    top_3_chaves = frequencias_chaves[:3]

    # Printa os top 3 resultados mais prováveis
    for freq, chave in top_3_chaves:
        texto_decifrado = ''
        for letra in texto_cifrado:
            if letra in ALFABETO:
                indice = (ALFABETO.find(letra) - chave) % len(ALFABETO)
                texto_decifrado += ALFABETO[indice]
            else:
                texto_decifrado += letra
        print(f'CHAVE: {chave} - Pontuação: {freq}\nTexto decifrado: {texto_decifrado}\n')

print('Programa para descriptografar César com base no peso das frequências das letras mais usadas no português')
print('\nEste programa retornará 3 possíveis resultados com suas respectivas chaves')
texto_cifrado = input('\nDigite o texto que deseja descriptografar: ')
#texto_cifrado = 'Kjqne fvzjqj vzj ywfsxkjwj t vzj xfgj j fuwjsij t vzj jsxnsf. Htwf Htwfqnsf.'
decifrar_com_pesos(texto_cifrado)
