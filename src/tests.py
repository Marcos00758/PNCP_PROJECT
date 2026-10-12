import requests as rqs

def buscar_itens_contratacao(cnpj: str, ano: int, sequencial: int) -> list:
    """Request for the PNCP API all itens from a procurement.
    
    Parameters
    -------------
    .... faça o resto da docstring
    """

    url_itens = f"https://pncp.gov.br/api/consulta/v1/orgaos/{cnpj}/compras/{ano}/{sequencial}/itens"
    try:
        response = rqs.get(url_itens, timeout=(5,30))
        response.raise_for_status()
        dados_itens = response.json()
    except rqs.RequestException as erro:
        raise rqs.RequestException(f"Chamado de itens do cnpj {cnpj}, ano {ano} e sequencial {sequencial} gerou o erro {erro}") from erro

    return dados_itens

itens = buscar_itens_contratacao(
    "48198725000162",
    2025,
    52,
)

print(type(itens))
print(len(itens))
print(itens[0])