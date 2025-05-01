import requests
url = 'https://economia.awesomeapi.com.br/json/last/USD-BRL'

requesicao = requests.get(url)
def brl_para_dolar(valor):
    if requesicao.status_code == 200:
        dados = requesicao.json()
        cotacao_dolar = valor / float(dados['USDBRL']['bid']) 
        return f'{cotacao_dolar:.0f}'
    else:
        raise ConnectionError('Não foi possível se conectar a api')

####para brl
def dolar_para_brl(valor):
    if requesicao.status_code == 200:
        dados = requesicao.json()
        cotacao_brl = (valor * float(dados['USDBRL']['bid']))
        return f'{cotacao_brl:.0f}'
    else:
        raise ConnectionError('Não foi possível se conectar a api')

