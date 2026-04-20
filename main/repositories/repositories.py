import pandas as pd
import os
import openpyxl

class Repository:
    
    def __init__(self, services):
        self.services = services
        # Set path relative to this file location
        current_dir = os.path.dirname(os.path.abspath(__file__))  # repositories/
        parent_dir = os.path.dirname(current_dir)  # main/
        self.planilhas_path = os.path.join(parent_dir, "planilhas")
    
    def cratexlsx(self):

        try:

            self.dados = [
                self.services.id,
                self.services.codigo,
                self.services.nome, 
                self.services.descricao, 
                self.services.preco, 
                self.services.grupo, 
                self.services.subgrupo, 
                self.services.impressao, 
                self.services.ncm, 
                self.services.cest, 
                self.services.uncompra,
                self.services.unvendas, 
                self.services.pesavel, 
                self.services.fracionado,
                self.services.exportarbalanca, 
                self.services.classificacao 
            ]

    
            self.df = pd.DataFrame(columns=self.dados)
            output_path = os.path.join(self.planilhas_path, "Planilha_base.xlsx")
            self.df.to_excel(output_path, index=False)

            return True
    
        except Exception as e:
            print(f"\nErro ao criar planilha base: {e}\n")
            return False
        

    def datamigration(self, cliente):

      try:
        self.planilha_cliente = self.services.planilha_cliente

        self.df_base = pd.read_excel(os.path.join(self.planilhas_path, "Planilha_base.xlsx"))
        self.df_cliente = pd.read_excel(os.path.join(self.planilhas_path, f"{cliente}"))

        print(f"\nColunas disponíveis no arquivo cliente: {list(self.df_cliente.columns)}\n")

        # Map client columns to base template columns - only for non-empty column names
        if self.services.id_cliente:
            self.df_base[self.services.id] = self.df_cliente[self.services.id_cliente]
        if self.services.codigo_cliente:
            self.df_base[self.services.codigo] = self.df_cliente[self.services.codigo_cliente]
        if self.services.nome_cliente:
            self.df_base[self.services.nome] = self.df_cliente[self.services.nome_cliente]
        if self.services.descricao_cliente:
            self.df_base[self.services.descricao] = self.df_cliente[self.services.descricao_cliente]
        if self.services.preco_cliente:
            self.df_base[self.services.preco] = self.df_cliente[self.services.preco_cliente]
        if self.services.grupo_cliente:
            self.df_base[self.services.grupo] = self.df_cliente[self.services.grupo_cliente]
        if self.services.subgrupo_cliente:
            self.df_base[self.services.subgrupo] = self.df_cliente[self.services.subgrupo_cliente]
        if self.services.impressao_cliente:
            self.df_base[self.services.impressao] = self.df_cliente[self.services.impressao_cliente]
        if self.services.ncm_cliente:
            self.df_base[self.services.ncm] = self.df_cliente[self.services.ncm_cliente]
        if self.services.cest_cliente:
            self.df_base[self.services.cest] = self.df_cliente[self.services.cest_cliente]
        if self.services.uncompra_cliente:
            self.df_base[self.services.uncompra] = self.df_cliente[self.services.uncompra_cliente]
        if self.services.unvendas_cliente:
            self.df_base[self.services.unvendas] = self.df_cliente[self.services.unvendas_cliente]
        if self.services.pesavel_cliente:
            self.df_base[self.services.pesavel] = self.df_cliente[self.services.pesavel_cliente]
        if self.services.fracionado_cliente:
            self.df_base[self.services.fracionado] = self.df_cliente[self.services.fracionado_cliente]
        if self.services.exportarbalanca_cliente:
            self.df_base[self.services.exportarbalanca] = self.df_cliente[self.services.exportarbalanca_cliente]
        if self.services.classificacao_cliente:
            self.df_base[self.services.classificacao] = self.df_cliente[self.services.classificacao_cliente]
        

        self.df_base.to_excel(os.path.join(self.planilhas_path, "Planilha_migrada.xlsx"), index=False)
        
        print("\nMigração de dados concluída!\n")
        return True

      except KeyError as e:
         print(f"\nErro: Coluna não encontrada - {e}\n")
         print(f"Verifique se a coluna '{e}' existe no arquivo cliente.\n")
         return False
      except Exception as e:
         print(f"\nErro de migração de dados: {type(e).__name__}: {e}\n")
         import traceback
         traceback.print_exc()
         return False

      



        



    

        
    
        
        
