import requests
url = 'https://economia.awesomeapi.com.br/json/last/USD-BRL'

requesicao = requests.get(url)
def conversao(number):
    if requesicao.status_code == 200:
        dados = requesicao.json()
        cotacao_dolar = number / float(dados['USDBRL']['bid']) 
        return f'{cotacao_dolar:.0f}'
    else:
        print('deu pau')
