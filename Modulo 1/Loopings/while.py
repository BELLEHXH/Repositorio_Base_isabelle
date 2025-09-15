opção = 4
while opção != 3:
    
    opção = int (input(f"digite  :\n 1-criar usuario \n 2-logar \n 3- sair\n"))
    if opção == 1:
        usuario_cadastro = (input(f"voce deseja criar um usuario?"))
        senha_cadastro = (input(f"voce deseja logar alguma senha?"))
        print(f"conta criada")
    elif opção == 2:
        login = (input (f"digite o usuario: \n"))
        senha = (input(f"digite sua senha; \n"))
        login = (input(f"digite o {usuario} e {senha} para fazer o login"))
        if usuario == usuario_digitado and senha == senha_digitada:
            print(f"login bem sucedido")
    else:
        print(f"usuario ou senha incorreta.")
else:
        print(f" agradeçemos a seu login")

