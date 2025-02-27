import pandas as pd

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

df = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9, df10])
df["Valor"] = df["Valor"].str.replace(",",".") #troca , por . #necessário para contas
df = df.reset_index(drop=True)
df.to_excel("base.xlsx")

colunas = ["Valor", "Data Coleta", "Parametro"]

df_ph = df.loc[df["Parametro"] == "pH", colunas]
df_fos = df.loc[df["Parametro"] == "Fósforo Total", colunas]
df_nit = df.loc[df["Parametro"] == "Nitrogênio Kjeldahl", colunas].reset_index(drop=True)
df_nit_k = df.loc[df["Parametro"] == "Nitrogênio Kjeldahl", "Valor"].astype('float32').reset_index(drop=True)
df_nit_no = df.loc[df["Parametro"] == "Nitrogênio-Nitrito", "Valor"].astype('float32').reset_index(drop=True)
df_nit_na = df.loc[df["Parametro"] == "Nitrogênio-Nitrato", "Valor"].astype('float32').reset_index(drop=True)
df_aux = df_nit_no + df_nit_na + df_nit_k
df_aux = df_aux.dropna()
df_nit["Parametro"] = "Nitrogenio Total"
df_nit["Valor"] = df_aux.values

df_coliformes = df.loc[df["Parametro"] == "Escherichia coli**", colunas] #verificar
df_turbo = df.loc[df["Parametro"] == "Turbidez", colunas]
df_res = df.loc[df["Parametro"] == "Sólido Total", colunas] #verificar
df_oxi = df.loc[df["Parametro"] == "Oxigênio Dissolvido", colunas]
df_temp = df.loc[df["Parametro"] == "Temperatura do Ar", colunas].reset_index(drop=True)
df_temp_ar = df.loc[df["Parametro"] == "Temperatura do Ar", "Valor"].astype('float32').reset_index(drop=True)
df_temp_agua = df.loc[df["Parametro"] == "Temperatura da Água", "Valor"].astype('float32').reset_index(drop=True)
df_aux = df_temp_ar.subtract(df_temp_agua)
df_temp["Parametro"] = "Delta Temperatura"
df_temp["Valor"] = df_aux.values

df_limpo = pd.concat([df_ph, df_fos, df_nit, df_coliformes, df_turbo, df_res, df_oxi, df_temp])

df_limpo.to_excel("df.xlsx")

#NAO TEM DBO!!!!!!!!!!!!