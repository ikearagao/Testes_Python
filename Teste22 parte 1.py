import random
#Exercicio1

jogoativo = 1
hiscore1 = hiscore2 = hiscore3 = 0
while True:
    while jogoativo == 1:
        tentativas = tentativastotais = loopaux = score = 0
        print ("==============================\n     JOGO DE ADIVINHAÇAO     \n==============================")
        dificuldade = int(input("Digite a dificuldade\n\nFácil[1] Médio[2] Difícil[3]: "))

        if dificuldade == 1:
            tentativastotais = 7
            numero = random.randint(1, 21)
            print("")
            while loopaux == 0:
                numerojogador = int(input(f"Digite um número entre 1 a 20. Você possui {tentativastotais} tentativas: "))
                tentativastotais -= 1
                if numerojogador == numero:
                    print("\nParabéns, voce acertou.\n")
                    score = 1000 + ((tentativastotais + 1) * (100))
                    if score > hiscore1:
                        hiscore1 = score
                    elif score > hiscore2:
                        hiscore2 = score
                    elif score > hiscore3:
                        hiscore3 = score
                    while loopaux == 0:
                        print("Gostaria de jogar novamente? (S/N)\n")
                        continuar = str(input(""))
                        if continuar == 's':
                            print("")
                            print (f"3 maiores pontuações: \n{hiscore1}\n{hiscore2}\n{hiscore3}\n")
                            loopaux += 1
                        elif continuar == 'n':
                            print("\nGAME OVER")
                            jogoativo += 1
                            loopaux += 1
                        else:
                            print("\nErro de digitação.")

                elif numerojogador < numero:
                    print(f"Incorreto. O número esperado é " + '\033[34m' + 'maior\n' + '\033[0m')
                elif numerojogador > numero:
                    print(f"Incorreto. O número esperado é " + '\033[31m' + 'menor\n' + '\033[0m')

                if tentativastotais == 0 and numerojogador != numero:
                    print("Não foi dessa vez...\n")
                    while loopaux == 0:
                        print("Gostaria de jogar novamente? (S/N)\n")
                        continuar = str(input(""))
                        if continuar == 's':
                            print("")
                            loopaux += 1
                        elif continuar == 'n':
                            print("\nGAME OVER")
                            jogoativo += 1
                            loopaux += 1
                        else:
                            print("\nErro de digitação.")


        elif dificuldade == 2:
            tentativastotais = 4
            numero = random.randint(1, 13)
            print("")
            while loopaux == 0:
                numerojogador = int(input(f"Digite um número entre 1 a 12. Você possui {tentativastotais} tentativas: "))
                tentativastotais -= 1
                if numerojogador == numero:
                    print("\nParabéns, voce acertou.\n")
                    score = 2000 + ((tentativastotais + 1) * (150))
                    if score > hiscore1:
                        hiscore1 = score
                    elif score > hiscore2:
                        hiscore2 = score
                    elif score > hiscore3:
                        hiscore3 = score
                    while loopaux == 0:
                        print("Gostaria de jogar novamente? (S/N)\n")
                        continuar = str(input(""))
                        if continuar == 's':
                            print("")
                            print(f"3 maiores pontuações: \n{hiscore1}\n{hiscore2}\n{hiscore3}\n")
                            loopaux += 1
                        elif continuar == 'n':
                            print("\nGAME OVER")
                            jogoativo += 1
                            loopaux += 1
                        else:
                            print("\nErro de digitação.")

                elif numerojogador < numero:
                    print(f"Incorreto. O número esperado é " + '\033[34m' + 'maior\n' + '\033[0m')
                elif numerojogador > numero:
                    print(f"Incorreto. O número esperado é " + '\033[31m' + 'menor\n' + '\033[0m')

                if tentativastotais == 0 and numerojogador != numero:
                    print("Não foi dessa vez...\n")
                    while loopaux == 0:
                        print("Gostaria de jogar novamente? (S/N)\n")
                        continuar = str(input(""))
                        if continuar == 's':
                            print("")
                            loopaux += 1
                        elif continuar == 'n':
                            print("\nGAME OVER")
                            jogoativo += 1
                            loopaux += 1
                        else:
                            print("\nErro de digitação.")

        elif dificuldade == 3:
            tentativastotais = 3
            numero = random.randint(1, 11)
            print ("")
            while loopaux == 0:
                numerojogador = int(input(f"Digite um número entre 1 a 10. Você possui {tentativastotais} tentativas: "))
                tentativastotais -= 1
                if numerojogador == numero:
                    print ("\nParabéns, voce acertou.\n")
                    score = 3000 + ((tentativastotais + 1) * (200))
                    if score > hiscore1:
                        hiscore1 = score
                    elif score > hiscore2:
                        hiscore2 = score
                    elif score > hiscore3:
                        hiscore3 = score
                    while loopaux == 0:
                        print ("Gostaria de jogar novamente? (S/N)\n")
                        continuar = str(input(""))
                        if continuar == 's':
                            print("")
                            print(f"3 maiores pontuações: \n{hiscore1}\n{hiscore2}\n{hiscore3}\n")
                            loopaux += 1
                        elif continuar == 'n':
                            print("\nGAME OVER")
                            jogoativo += 1
                            loopaux += 1
                        else:
                            print ("\nErro de digitação.")

                elif numerojogador < numero:
                    print(f"Incorreto. O número esperado é " + '\033[34m' + 'maior\n' + '\033[0m')
                elif numerojogador > numero:
                    print(f"Incorreto. O número esperado é " + '\033[31m' + 'menor\n' + '\033[0m')

                if tentativastotais == 0 and numerojogador != numero:
                    print ("Não foi dessa vez...\n")
                    while loopaux == 0:
                        print ("Gostaria de jogar novamente? (S/N)\n")
                        continuar = str(input(""))
                        if continuar == 's':
                            print("")
                            loopaux += 1
                        elif continuar == 'n':
                            print("\nGAME OVER")
                            jogoativo += 1
                            loopaux += 1
                        else:
                            print ("\nErro de digitação.")

        else:
            while loopaux == 0:
                print ("\nErro de digitação. Gostaria de tentar novamente? (S/N): ")
                continuar = str(input(""))
                if continuar == 's':
                    print ("")
                    loopaux += 1
                elif continuar == 'n':
                    print ("\nGAME OVER")
                    jogoativo += 1
                    loopaux += 1

    break