def ler_livro_com_mika():
    print("lendo livro com a mikinha\n\n")
def nao_ler_livro_com_mika():
    ...
opção = 0
while opção != 3:
    ler = int(input(f"voce quer ler um livro com a mika? \n 1-sim \n2-não \n"))
    if ler == 1:
        ler_livro_com_mika()
    else:
        print (f"af,tchau")
     
