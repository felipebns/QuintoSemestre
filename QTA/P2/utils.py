## NOTA: TEMPERATURA DA AGUA

tabela_conversao = {
    0: 14.6,
    1: 14.2,
    2: 13.8,
    3: 13.5,
    4: 13.1,
    5: 12.8,
    6: 12.5,
    7: 12.2,
    8: 11.9,
    9: 11.6, 
    10: 11.3,
    11: 11.1,
    12: 10.9,
    13: 10.6,
    14: 10.4,
    15: 10.2,
    16: 10.0,
    17: 9.8,
    18: 9.6,
    19: 9.4,
    20: 9.2,
    21: 9.0,
    22: 8.9,
    23: 8.7,
    24: 8.6,
    25: 8.4,
    26: 8.2,
    27: 8.1,
    28: 7.9,
    29: 7.8,
    30: 7.7
}

def converte_porc(temp_agua, concentracao_atual):
    floating = float(temp_agua) - int(float(temp_agua))

    if (floating > 0.5):
        temp_agua = int(float(temp_agua)) + 1
    else:
        temp_agua = int(float(temp_agua))

    concentracao_saturacao = tabela_conversao[temp_agua]

    return (float(concentracao_atual)/concentracao_saturacao)*100