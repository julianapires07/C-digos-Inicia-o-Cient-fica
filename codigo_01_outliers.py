import numpy as np

def remover_outliers_recursivamente(dados):
    while True:
        q1 = np.percentile(dados, 25)
        q3 = np.percentile(dados, 75)
        iqr = q3 - q1
        lim_inf = q1 - 1.5 * iqr
        lim_sup = q3 + 1.5 * iqr
        dados_filtrados = dados[(dados >= lim_inf) & (dados <= lim_sup)]

        if len(dados_filtrados) == len(dados):
            break
        dados = dados_filtrados
    return dados

def analisar_dados():
    print("Cole seus dados do Excel abaixo (valores em linhas ou colunas).")
    print("Pressione ENTER em branco para terminar a entrada de dados:\n")

    linhas = []
    while True:
        linha = input()
        if linha.strip() == "":
            break
        linhas.append(linha)

    # Junta todas as linhas e separa por espaços
    dados_str = " ".join(linhas).replace(",", " ").replace("\t", " ")

    try:
        dados = np.array([float(x) for x in dados_str.split()])
    except ValueError:
        print(" Erro: Verifique se todos os dados são números válidos.")
        return

    if len(dados) == 0:
        print(" Nenhum dado inserido.")
        return

    dados_limpos = remover_outliers_recursivamente(dados)

    # No máximo 256
    if len(dados_limpos) > 256:
        dados_limpos = dados_limpos[:256]

    # Ressult
    media = np.mean(dados_limpos)
    q1 = np.percentile(dados_limpos, 25)
    q2 = np.median(dados_limpos)
    q3 = np.percentile(dados_limpos, 75)
    iqr = q3 - q1
    lim_inf = q1 - 1.5 * iqr
    lim_sup = q3 + 1.5 * iqr

    print("\n--- RESULTADOS ---")
    print(f"Qtd original: {len(dados)}")
    print(f"Qtd após remoção de outliers: {len(dados_limpos)}")
    print(f"Média: {round(media)}")
    print(f"Mediana (Q2): {round(q2)}")
    print(f"Q1: {round(q1)}")
    print(f"Q3: {round(q3)}")
    print(f"IQR: {round(iqr)}")
    print(f"Limite inferior: {round(lim_inf)}")
    print(f"Limite superior: {round(lim_sup)}")

    print("\n Dados finais (prontos para colar no Excel):")
    print("\n".join([str(round(x)) for x in dados_limpos]))


analisar_dados()


