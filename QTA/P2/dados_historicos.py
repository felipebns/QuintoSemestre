from utils import *
import pandas as pd
import matplotlib.pyplot as plt

# Baixando
df1 = pd.read_excel("DadosG1.xlsx")
df2 = pd.read_excel("DadosG2.xlsx")
df3 = pd.read_excel("DadosG3.xlsx")
df4 = pd.read_excel("DadosG4.xlsx")
df5 = pd.read_excel("DadosG5.xlsx")
df6 = pd.read_excel("DadosG6.xlsx")
df7 = pd.read_excel("DadosG7.xlsx")
df8 = pd.read_excel("DadosG8.xlsx")
df9 = pd.read_excel("DadosG9.xlsx")
df10 = pd.read_excel("DadosG10.xlsx")

#Concatena em um grande df e limpa
df = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9, df10])
df["Valor"] = df["Valor"].str.replace(",",".") #troca , por . #necessário para contas
df = df.reset_index(drop=True)
df.to_excel("df_base.xlsx")

#Colunas desejadas
colunas = ["Valor", "Data Coleta", "Parametro", "Unidade"]

#df PH
df_ph = df.loc[df["Parametro"] == "pH", colunas].drop_duplicates('Data Coleta',keep='first')

#df do fósforo total
df_fos = df.loc[df["Parametro"] == "Fósforo Total", colunas].drop_duplicates('Data Coleta',keep='first')

#df do nitrogênio total 
df_nit = df.loc[df["Parametro"] == "Nitrogênio Kjeldahl", colunas].reset_index(drop=True)
df_nit_k = df.loc[df["Parametro"] == "Nitrogênio Kjeldahl", "Valor"].astype('float32').reset_index(drop=True)
df_nit_no = df.loc[df["Parametro"] == "Nitrogênio-Nitrito", "Valor"].astype('float32').reset_index(drop=True)
df_nit_na = df.loc[df["Parametro"] == "Nitrogênio-Nitrato", "Valor"].astype('float32').reset_index(drop=True)
df_aux = df_nit_no + df_nit_na + df_nit_k
df_aux = df_aux.dropna()
df_nit["Parametro"] = "Nitrogenio Total"
df_nit["Valor"] = df_aux.values
df_nit = df_nit.drop_duplicates('Data Coleta',keep='first')

#df dos coliformes fecais (mais próximo possível)
df_coliformes = df.loc[df["Parametro"] == "Escherichia coli**", colunas] .drop_duplicates('Data Coleta',keep='first')

#df turbidez da água
df_turbo = df.loc[df["Parametro"] == "Turbidez", colunas].drop_duplicates('Data Coleta',keep='first')

#df resíduos totais (mais próximo possível)
df_res = df.loc[df["Parametro"] == "Sólido Total", colunas].drop_duplicates('Data Coleta',keep='first') #pode funcionar

#df delta temperatura
df_temp = df.loc[df["Parametro"] == "Temperatura da Água", colunas].reset_index(drop=True)
df_copia_temp = df_temp.drop_duplicates('Data Coleta',keep='first')
df_temp_ar = df.loc[df["Parametro"] == "Temperatura do Ar", "Valor"].astype('float32').reset_index(drop=True)
df_temp_agua = df.loc[df["Parametro"] == "Temperatura da Água", "Valor"].astype('float32').reset_index(drop=True)
df_aux = df_temp_ar.subtract(df_temp_agua)
df_temp["Parametro"] = "Delta Temperatura"
df_temp["Valor"] = df_aux.values
df_temp = df_temp.drop_duplicates('Data Coleta',keep='first')

#df oxigênio dissolvido
df_oxi_conc = df.loc[df["Parametro"] == "Oxigênio Dissolvido", colunas].drop_duplicates('Data Coleta',keep='first') #CONVERTER UNIDADE
df_oxi_porc = df_oxi_conc

list_oxi_conc = pd.Series(df_oxi_conc['Valor']).reset_index(drop=True)
list_temp_agua = pd.Series(df_copia_temp['Valor']).reset_index(drop=True)
list_oxi_porc = []

for i,e in enumerate(list_oxi_conc):
    list_oxi_porc.append(converte_porc(list_temp_agua[i], e))

df_oxi_porc["Unidade"] = "% Saturacao"
df_oxi_porc["Valor"] = list_oxi_porc

#df novo
df_limpo = pd.concat([df_ph, df_fos, df_nit, df_coliformes, df_turbo, df_res, df_oxi_porc, df_temp]).reset_index(drop=True)

df_limpo.to_excel("df_clean.xlsx")

df_ph = df_ph.reset_index(drop=True)
df_ph_data = pd.to_datetime(df["Data Coleta"], dayfirst=True, errors="coerce")
df_ph_data = pd.to_datetime(df_ph_data, format='%d/%m/%y')
plt.plot(df_ph_data,df_ph["Valor"])
plt.xticks(rotation=90)
plt.show()


#NAO TEM DBO!!!!!!!!!!!!