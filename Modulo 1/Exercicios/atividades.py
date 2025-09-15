gaveta = []
opção = 0
while opção !=5:
    opção = int (input("digite o que voce deseja fazer :\n 1-ver gaveta \n 2-adicionar na gaveta \n 3-tirar da gaveta \n 4-modificar \n 5-sair "))
    if opção == 1:
        print (f"itens da gaveta: \n {gaveta}")
    elif opção ==2:
        item = input("digite o nome do que voce quer ser adicionado: \n")
        gaveta.append (item)
    elif opção ==3: 
         item = input("seu item foi retirado: \n")
    elif opção == 4:
        item = input("seu item foi modificado: \n")
    else:
        print("voce saiu")
        
