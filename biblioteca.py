class Biblioteca:
    #def __init__(self, login, cadastro, )





    def mostraMenu(self):
        menuInicial = """
    ==================================
            BIBLIOTECA DIGITAL  
    ==================================
    
    1 - Login
    2 - Cadastrar Usuário
    3 - Consultar Livros
    0 - Sair
    """
        print(menuInicial)
        print()
        opcao = int(input("Digite a opcao desejada: "))

        match opcao:
            case 1: 
                login()
            case 2:
                cadastrarUsuario()
            case 3:
                consultarLivro()
            case 4: 
                sair()
            case _:
                print("Opção inválida!")
    
    def login(self):
        pass

    def cadastrarUsuario(self):
        pass

    def cadastrarLivro(self):
        pass

    def consultarLivro(self):
        pass

    def emprestarLivro(self):
        pass

    def devolverLivro(self):
        pass

    def meusEmprestimos(self):
        pass

    def sair(self):
        print("Obrigado por usar a Biblioteca Digital!")
