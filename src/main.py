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
print(dados_publicacao["totalPaginas"])
# for indice, contratacao in enumerate(dados_publicacao["data"], start=1):
#     razao_social = contratacao["orgaoEntidade"]["razaoSocial"]
#     municipio_nome = contratacao["unidadeOrgao"]["municipioNome"]
#     objeto_compra = contratacao["objetoCompra"]
#     valor_total_estimado = contratacao['valorTotalEstimado']
#     valor_total_homologado = contratacao["valorTotalHomologado"]

#     dict_de_dados = {
#     "razao_social": razao_social,
#     "municipio": municipio_nome,
#     "objeto_compra": objeto_compra,
#     "valor_total_estimado": valor_total_estimado,
#     "valor_total_homologado": valor_total_homologado
# }
#     print(indice, ": ")
#     for chave, item in dict_de_dados.items():
#         if item is None:
#             print(f"{chave} esta vazio na contratação {indice}")
#         else:
#             print(item)
