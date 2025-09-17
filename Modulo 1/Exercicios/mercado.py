o_que_comprar = ["arroz","feijão","cenoura","bife"]
opção = 0
while opção !=5:
    
    opção = int (input(f"digite o que voce deseja fazer :\n 1-ver carrinho de compras \n 2-adicionar no carrinho \n 3-tirar do carrinho \n 4- atualizar as compras "))
    if opção == 1:
        print(f"itens do carrinho de compras: | {o_que_comprar}")
    elif opção == 2:
       item = input("digite o que voce quer adicionar :\n")
       o_que_comprar.append (item)
    elif opção == 3:
       item = input ("seu item foi retirado do carrinho :\n")
    elif opção == 4:
        item = input ("qual item da lista voce quer atualizar?")
        novo_item = input("digite o novo item:")
    else:
        print(f"novo item atualizado")





    




