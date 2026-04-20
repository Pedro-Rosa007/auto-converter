
import pandas
from repositories.repositories import Repository
from time import sleep



class Services:




    def __init__(self):

        self.builder()


    def builder(self):

        self.default_collumns()
        self.datainsert()



    def default_collumns(self):



        self.id = str("ID")
        self.codigo = str("Codigo")
        self.nome = str("Nome")
        self.descricao = str("Descrição")
        self.preco = str("Preço")
        self.grupo = str("Grupo")
        self.subgrupo = str("Subgrupo")
        self.impressao = str("Local Impressão")
        self.ncm = str("NCM")
        self.cest = str("CEST")
        self.uncompra= str("Un Compra")
        self.unvendas = str("Un Vendas")
        self.pesavel = str("PESAVEL")
        self.fracionado = str("FRACIONADO")
        self.exportarbalanca = str("EXPORTAR BALANÇA")
        self.classificacao = str("Nome Classificação Fiscal")











    def catch_collumns(self):
     
     self.endpoint_1 = False


     while True:


        self.id_cliente = input("\nInsira a coluna relativa aos ID's dos produtos\n")
        if self.id_cliente.isdigit():
            print("\nInsira um nome válido!\n")
        else:
            pass
        

        self.codigo_cliente = input("\nInsira a coluna relativa aos Codigos dos produtos\n")
        if self.codigo_cliente.isdigit():
            print("\nInsira um nome válido!\n")
        else: 
            pass


        self.nome_cliente = input("\nInsira a coluna relativa aos Nomes dos produtos\n")
        if self.nome_cliente == "" or self.nome_cliente.isdigit():
            print("\nInsira um nome válido!\n")
        else: 
            pass


        self.descricao_cliente = input("\nInsira a coluna relativa as Descrições dos produtos\n")
        if self.descricao_cliente.isdigit():
            print("\nInsira um nome válido!\n")
        else: 
            pass


        self.preco_cliente = input("\nInsira a coluna relativa aos Preços dos produtos\n")
        if self.preco_cliente == "" or self.preco_cliente.isdigit():
            print("\nInsira um nome válido!\n")
        else: 
            pass


        self.grupo_cliente = input("\nInsira a coluna relativa aos Grupos dos produtos\n")
        if self.grupo_cliente == "" or self.grupo_cliente.isdigit():
            print("\nInsira um nome válido!\n")
        else: 
            pass


        self.subgrupo_cliente = input("\nInsira a coluna relativa aos Subgrupos dos produtos\n")
        if self.subgrupo_cliente == "" or self.subgrupo_cliente.isdigit():
            print("\nInsira um nome válido!\n")
        else: 
            pass


        self.impressao_cliente = input("\nInsira a coluna relativa aos Locais de Impressão dos produtos\n")
        if self.impressao_cliente == "" or self.impressao_cliente.isdigit():
            print("\nInsira um nome válido!\n")
        else: 
            pass


        self.ncm_cliente = input("\nInsira a coluna relativa ao NCM dos produtos\n")
        if self.ncm_cliente.isdigit():
            print("\nInsira um nome válido!\n")
        else: 
            pass




        self.cest_cliente = input("\nInsira a coluna relativa ao CEST dos produtos\n")
        if self.cest_cliente.isdigit():
            print("\nInsira um nome válido!\n")
        else: 
            pass



        self.uncompra_cliente = input("\nInsira a coluna relativa a Unidade De Compra dos produtos\n")
        if self.uncompra_cliente.isdigit():
            print("\nInsira um nome válido!\n")
        else: 
            pass

        


        self.unvendas_cliente = input("\nInsira a coluna relativa a Unidade De Vendas dos produtos\n")
        if self.unvendas_cliente.isdigit():
            print("\nInsira um nome válido!\n")
        else: 
            pass
        


        self.pesavel_cliente = input("\nInsira a coluna relativa a Pesagem dos produtos\n")
        if self.pesavel_cliente.isdigit():
            print("\nInsira um nome válido!\n")
        else: 
            pass
        


        self.fracionado_cliente = input("\nInsira a coluna relativa a Fracionação dos produtos\n")
        if self.fracionado_cliente.isdigit():
            print("\nInsira um nome válido!\n")
        else: 
            pass



        self.exportarbalanca_cliente = input("\nInsira a coluna relativa a Balança dos produtos\n")
        if self.exportarbalanca_cliente.isdigit():
            print("\nInsira um nome válido!\n")
        else: 
            pass



        self.classificacao_cliente = input("\nInsira a coluna relativa a Classificação Fiscal dos produtos\n")
        if self.classificacao_cliente.isdigit():
            print("\nInsira um nome válido!\n")
        else: 
            self.endpoint_1 = True
            break






    def createnewdata(self):

        try:
            self.catch_collumns()

            while True:
                self.planilha_cliente = input("\nInsira o nome da planilha do cliente, por exemplo: exemplo.xlsx\n")
                print("Insira a planilha na pasta Planilhas!")
                if self.planilha_cliente == "" or self.planilha_cliente.isdigit():
                    print("\nInsira caminho válido!\n")
                else:
                    break

            # Create base file
            repo = Repository(self)
            if repo.cratexlsx():
                print("\nPlanilha Base criada!\n")
            else:
                print("\nErro ao criar Planilha Base\n")
                return False

            return True
            
        except Exception as e:
            print(f"\nErro ao criar Planilha Base: {e}\n")
            return False




    def datainsert(self):

        self.createnewdata()
        repo = Repository(self)
        migracao = repo.datamigration(self.planilha_cliente)
        if migracao:
            print("\nPrograma encerrando...\n")
            sleep(2)
            exit()
        else:
            print("\nErro, Reinicie o programa ou contate seu desenvolvedor!\n")


    
        
     








Services()
