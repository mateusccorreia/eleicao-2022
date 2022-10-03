import requests
import json
import pandas as pd

data = requests.get(
    'https://resultados.tse.jus.br/oficial/ele2022/544/dados-simplificados/br/br-c0001-e000544-r.json')
json_data = json.loads(data.content)

candidato = []
num = []
partido = []
votos = []
porcentagem = []
for informacoes in json_data['cand']:

    if informacoes['seq'] == '1' or informacoes['seq'] == '2' or informacoes['seq'] == '3' or informacoes['seq'] == '4':
        candidato.append(informacoes['nm'])
        num.append(informacoes['n'])
        votos.append(informacoes['vap'])
        porcentagem.append(informacoes['pvap'])
                

df_eleicao = pd.DataFrame(list(zip(candidato, num, votos, porcentagem)), columns=[
    'Candidato', 'Numero', 'N Votos', 'Porcentagem'])

print(df_eleicao)
                         
                         
