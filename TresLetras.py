# Nome: Lucas Lima Aires
import string

def testa_a(texto_cifrado_u):
    # Descobre a chave
    chave = (ord(letra_mais_frequente)) - ord('A')
    if(chave < 0):
        chave = chave + 26
    
    # Se a letra for A, decodifica de acordo com a chave
    for letra in texto_cifrado_u:
        if letra == 'A':
            posicao = alfabeto.find(letra)
            nova_posicao = (posicao - chave) % 26
            novo_caracter = alfabeto[nova_posicao]
        
    
    texto_decifrado = ""

    # Troca o resto das letras, e apaga caracteres especiais
    for letra in texto_cifrado_u:
        texto_cifrado_u = texto_cifrado_u.replace(letra_mais_frequente, 'A')
        if letra not in alfabeto:
            texto_decifrado += ' '
            continue
        elif letra != 'A':
            posicao = alfabeto.find(letra)
            nova_posicao = (posicao - chave) % 26
            novo_caracter = alfabeto[nova_posicao]
            texto_decifrado += novo_caracter
    print('\nTexto decifrado com base na letra A: '+texto_decifrado+ '\nChave: '+str(chave))
        
def testa_e(texto_cifrado_u):
    # Descobre a chave
    chave = (ord(letra_mais_frequente)) - ord('E')
    if(chave < 0):
        chave = chave + 26
    
    # Se a letra for E, decodifica de acordo com a chave
    for letra in texto_cifrado_u:
        if letra == 'E':
            posicao = alfabeto.find(letra)
            nova_posicao = (posicao - chave) % 26
            novo_caracter = alfabeto[nova_posicao]
        
    
    texto_decifrado = ""

    # Troca o resto das letras, e apaga caracteres especiais
    for letra in texto_cifrado_u:
        texto_cifrado_u = texto_cifrado_u.replace(letra_mais_frequente, 'E')
        if letra not in alfabeto:
            texto_decifrado += ' '
            continue
        elif letra!= 'E':
            posicao = alfabeto.find(letra)
            nova_posicao = (posicao - chave) % 26
            novo_caracter = alfabeto[nova_posicao]
            texto_decifrado += novo_caracter
    print('\nTexto decifrado com base na letra E: '+texto_decifrado+ '\nChave: '+str(chave))


def testa_o(texto_cifrado_u):
    # Descobre a chave
    chave = ord(letra_mais_frequente) - ord('O')
    if(chave < 0):
        chave = chave + 26

    # Se a letra for O, decodifica de acordo com a chave
    for letra in texto_cifrado_u:
        if letra == 'O':
            posicao = alfabeto.find(letra)
            nova_posicao = (posicao - chave) % 26
            novo_caracter = alfabeto[nova_posicao]

    texto_decifrado = ""

    # Troca o resto das letras, e apaga caracteres especiais
    for letra in texto_cifrado_u:
        texto_cifrado_u = texto_cifrado_u.replace(letra_mais_frequente, 'O')
        if letra not in alfabeto:
            texto_decifrado += ' '
            continue
        elif letra != 'O':
            posicao = alfabeto.find(letra)
            nova_posicao = (posicao - chave) % 26
            novo_caracter = alfabeto[nova_posicao]
            texto_decifrado += novo_caracter
    print('\nTexto decifrado com base na letra O: '+texto_decifrado+ '\nChave: '+str(chave))
#####################################################################################################################################
print('Progama que descriptografa César com base nas 3 letras mais frequentes da língua Portuguesa')
texto_cifrado = input('Digite um texto cifrado: ')

alfabeto = string.ascii_uppercase

# Conta as letras do input 
letras = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0, 'J':0, 
          'K':0, 'L':0, 'M':0, 'N':0, 'O':0, 'P':0, 'Q':0, 'R':0, 'S':0, 'T':0, 
          'U':0, 'V':0, 'W':0, 'X':0, 'Y':0, 'Z':0}

for letra in texto_cifrado.upper():
    if letra in letras:
        letras[letra] += 1

# Ordena a lista em ordem decrescente
letras_ordenadas = sorted(letras.items(), key=lambda x: x[1], reverse=True)

# Joga todo o input para maiúsculo e pega a letra mais frequente do input
texto_cifrado_u = texto_cifrado.upper()
letra_mais_frequente = letras_ordenadas[0][0]

testa_a(texto_cifrado_u)
testa_e(texto_cifrado_u)
testa_o(texto_cifrado_u)
