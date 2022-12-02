#Exercicio2
palavra = str(input("Digite a palavra a ser descoberta: "))
vidas = 5
forca = []
forcadescoberta = []
for letra in palavra:
    forca.append(letra)

print (forca)

for i in range(0, len(forca)):
    forcadescoberta.append("_")

print (forcadescoberta)
print ()

while True:
    print("=========================\n     JOGO DA FORCA     \n=========================\n")
    print (f"Vidas do jogador: {vidas}")
    print ("Progresso atual na palavra: ", end= '')
    for j in range (0, len(forcadescoberta)):
        print (forcadescoberta[j], end='')
    print ("\n")

    acao = int(input("Digite [1] para tentar adivinhar uma letra ou [2] para tentar adivinhar uma palavra: "))

    if acao == 1:
        tentativa = str(input("Digite a próxima letra pra forca: "))
        if tentativa in forca:
            for k in range(0, len(forca)):
                if forca[k] == tentativa:
                    forcadescoberta[k] = forca[k]
                    print (f"Letra encontrada na posicao: {k + 1}")
            print ()
        else:
            print ("\nA letra não esta presente.\n")
            vidas -= 1
    elif acao == 2:
        adivinhacao = str(input("Digite a palavra: "))
        if adivinhacao == palavra:
            print("Você acertou!")
            print(f"A palavra era: ")
            for j in range(0, len(forcadescoberta)):
                print(forcadescoberta[j], end='')
            print()
            break
        else:
            print ("Você errou!\n")
            vidas -= 1
    else:
        print ("Ação inválida. Tente novamente\n")

    if vidas == 0:
        print ("Você perdeu!")
        break

    if forcadescoberta == forca:
        print("Você acertou!")
        print(f"A palavra era: ")
        for j in range(0, len(forcadescoberta)):
            print(forcadescoberta[j], end='')
        print()
        break