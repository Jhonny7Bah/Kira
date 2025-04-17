import requests
url = 'https://economia.awesomeapi.com.br/json/last/USD-BRL'

requesicao = requests.get(url)
number = 300
if requesicao.status_code == 200:
    dados = requesicao.json()
    cotacao_dolar = number / float(dados['USDBRL']['bid']) 
    print(f'{cotacao_dolar:.0f}')
else:
    print('deu pau')