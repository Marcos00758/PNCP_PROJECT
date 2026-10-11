import requests as rqs

url_contratacao = "https://pncp.gov.br/api/consulta/v1/contratacoes/publicacao"
params_publicacao = {"dataInicial": 20250501,
                     "dataFinal": 20250510,
                     "codigoModalidadeContratacao": 6,
                     "uf": "SP",
                     "pagina": 1}
    
response = rqs.get(url_contratacao, params=params_publicacao)
dados_publicacao = response.json()
print(type(dados_publicacao))
print(dados_publicacao.keys())
print(type(dados_publicacao["data"]))
print(len(dados_publicacao["data"]))
print(dados_publicacao["totalRegistros"])
print(dados_publicacao["data"][0])
print(dados_publicacao["data"][0].keys())

for indice, contratacao in enumerate(dados_publicacao["data"], start=1):
    razaoSocial = contratacao["orgaoEntidade"]["razaoSocial"]
    municipioNome = contratacao["unidadeOrgao"]["municipioNome"]
    objetoCompra = contratacao["objetoCompra"]
    valorTotalEstimado = contratacao['valorTotalEstimado']
    valorTotalHomologado = contratacao["valorTotalHomologado"]

    lista_de_dados = [razaoSocial, municipioNome, objetoCompra, valorTotalEstimado, valorTotalHomologado]    
    print(indice, ": ")
    for item in lista_de_dados:
        if item == None:
            print(f"{item=} esta vazio na contratação {indice}")
        else:
            print(item)
