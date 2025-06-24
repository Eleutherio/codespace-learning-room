print("Bem-vindo ao SimpleBank")

Saldo_CC = 0
Usuario = "Guilherme"
Extrato = 3
Saque = 2
Deposito = 1
menu = [Extrato, Saque, Deposito]
UsuarioSelecionouOpçao = False

def authenticator(input_usuario):
    if input_usuario == Usuario:
        print("Acesso liberado")
        return True
    else:
        print("Acesso negado")
        return False

# loop até acertar o nome
acesso = False
while not acesso:
    Registro = input("Digite seu usuário: ")
    acesso = authenticator(Registro)

print("Entrou no sistema. Olá ", Usuario , ". Seu saldo é de " , Saldo_CC , " Reais.")

Extrato = 3
Saque = 2
Deposito = 1
menu = [Extrato, Saque, Deposito]
UsuarioSelecionouOpçao = False

def authenticator(input_usuario):
    if input_usuario in menu:
        print ("Voce escolheu ", input_usuario)
        return True
    else:
        print ("Opção inválida. Digite alguma das opções abaixo")
        return False

while not UsuarioSelecionouOpçao:
    
    print("Depósito digite 1"),
    print("Saque digite 2"),
    print("Extrato digite 3"),
    
    opçao_digitada = int(input("Digite uma opção:"))
    
    UsuarioSelecionouOpçao = authenticator(opçao_digitada)
