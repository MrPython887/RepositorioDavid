palavra = "tempestade"
letras_inseridas = []
tentativas = 5
ganhou = False


while True:
    for letra in palavra:
        if letra.lower() in letras_inseridas:
            print(letra, end=" ")
        else:
            print("_", end =" ")
    print("Você tem {}".format(tentativas))
    

    #logica do jogo

tentativa = input("Escolha uma letras para a palavra secreta: ") 
letras_inseridas.append(tentativa.lower())
if tentativa.lower() not in palavra.lower():
    tentativas -= 1

ganhou = True

for letra in palavra:
        if letra.lower() not in letras_inseridas:
             
         ganhou = False    

if tentativas == 0 or ganhou:
     
    break

if ganhou:

            print("Parabéns, acertou a palavra secreta. A palavra secreta era: {}".format(palavra))

else:

    print("Você perdeu! A palavra secreta era: {}".format(palavra))
