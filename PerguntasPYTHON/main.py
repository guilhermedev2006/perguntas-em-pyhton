#jogo simples de perguntas em python com uso de if e else!

print("Seja Bem-Vindo ao Jogo de Perguntas!")

player = input("Digite seu nome: ")

print("-----------------------------------------")

print(player + ", 2 + 2 é igual a 4?")
escolha = input("1 para SIM e 2 para NAO: ")

if  escolha == "1":
    print("RESPOSTA CERTA!")
else:
    print("RESPOSTA ERRADA!")

print("-----------------------------------------")

print(player + ", 5 x 5 é igual a 25?")
escolha = input("1 para SIM e 2 para NAO: ")

if  escolha == "1":
    print("RESPOSTA CERTA!")
else:
    print("RESPOSTA ERRADA!")

print("-----------------------------------------")

print(player + ", 50 x 50 é igual a 900?")
escolha = input("1 para SIM e 2 para NAO: ")

if  escolha == "2":
    print("RESPOSTA CERTA!")
else:
    print("RESPOSTA ERRADA!")

print("-----------------------------------------")

print("FIM DO JOGO DE PERGUNTAS!")
print("OBRIGADO POR JOGAR, " + player)