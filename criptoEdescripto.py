#sub
def descriptografada(mensagem, avanço, cripto):
    contador = 0
    mensagem = ""
    for letra in cripto:
        mensagem = mensagem + chr((ord(letra)) + int(avanço[contador])*-1)
        contador =+ 1
        if contador == len(avanço):
            contador = 0
    return mensagem

def gerarCriptografada(mensagem, avanço):
    contador = 0
    cripto = ""
    for letra in mensagem:
        cripto = cripto + chr(ord(letra) + int(avanço[contador]))
        contador =+ 1
        if contador == len(avanço):
            contador = 0
    return cripto
def menu():
    print("SELECIONE UMA DAS OPÇÕES \n[1] Criptografar \n[2] Descriptografar \n[3] Encerrar programa")
    opcao = int(input("Opção escolhida:"))
    return opcao
def clear():
    apagar = input("Digite qualquer tecla para limpar")
    for n in range (100):
        print(" ")
#principal
opcao = menu()
print(opcao)
while opcao != 3:
    if opcao == 1:
        mensagem = input("Qual a mensagem a ser criptografada?")
        avanço = (input("Qual a chave de avanço"))
        cripto = gerarCriptografada(mensagem,avanço)
        print(f"A mensagem criptografada é {cripto}") 
        clear()
        opcao = menu()
        clear()
    elif opcao == 2:
        cripto = input("Qual a mensagem a ser descriptografada?")
        avanço = (input("Qual a chave de avanço"))
        mensagem = ""
        descripto = descriptografada(mensagem, avanço, cripto)
        print(f"A mensagem descriptografada é {descripto}")
        clear()
        opcao = menu()
        clear()
    elif opcao == 3:
        print("Encerrando programa")
    else:
        print("Opcão inexistente, programa encerrado")
        opcao = 3
print("Programa encerrado, até logo!")
