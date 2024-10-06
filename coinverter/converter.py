import requests
import json

def cotacao(de, para, valor = 1):
    moeda_conversao = f'{de}-{para}'

    url = 'http://economia.awesomeapi.com.br/json/last/' + de + '-' + para

    cotacao = requests.get(url).content

    dic_contacao = json.loads(cotacao)

    print(dic_contacao)
    print(dic_contacao[f'{de}{para}']["bid"])
    return float(dic_contacao[f'{de}{para}']["bid"]) * valor 


print(cotacao(de = 'USD', para = 'BRL', valor = 10))