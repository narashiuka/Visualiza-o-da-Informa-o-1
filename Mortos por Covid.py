#Anteriormente foi instalada a biblioteca GeoPandas que será usada para plotar um gráfico logo mais
#Importamos todas tabela que serão usados 

import matplotlib.pyplot as plt; plt.rcdefaults() 
import numpy as np 
import pandas as pd 
import seaborn as sns
import plotly.graph_objects as go
import geopandas as gpd

from matplotlib import pyplot as plt
from pandas import read_csv

covid = pd.read_csv("E:/Gabriel/Documentos/Estudos/Cruzeiro do Sul/Visualização da Informação/Projeto/Atividade Visualização-da-Informação/Exercícios .py/Covid-19/covid19.csv")

#Dados retirados do site:
#https://brasil.io/dataset/covid19/caso_full/?page=3
#usando a tabela "covid19-8369e44a27c245e6892c18cf1606b3ec"


#Neste passo, iremos filtrar os dados, trazendo para seus respectivos estados uma 
#tabela contendo seus dados separados, facilitando assim uma manipulação mais a frente

estados = covid.loc[covid["place_type"]=='state']

ac = estados.loc[estados["state"]=='AC']
al = estados.loc[estados["state"]=='AL']
ap = estados.loc[estados["state"]=='AP']
am = estados.loc[estados["state"]=='AM']
ba = estados.loc[estados["state"]=='BA']
ce = estados.loc[estados["state"]=='CE']
df = estados.loc[estados["state"]=='DF']
es = estados.loc[estados["state"]=='ES']
go = estados.loc[estados["state"]=='GO']
ma = estados.loc[estados["state"]=='MA']
mt = estados.loc[estados["state"]=='MT']
ms = estados.loc[estados["state"]=='MS']
mg = estados.loc[estados["state"]=='MG']
pa = estados.loc[estados["state"]=='PA']
pb = estados.loc[estados["state"]=='PB']
pr = estados.loc[estados["state"]=='PR']
pe = estados.loc[estados["state"]=='PE']
pi = estados.loc[estados["state"]=='PI']
rj = estados.loc[estados["state"]=='RJ']
rn = estados.loc[estados["state"]=='RN']
rs = estados.loc[estados["state"]=='RS']
ro = estados.loc[estados["state"]=='RO']
rr = estados.loc[estados["state"]=='RR']
sc = estados.loc[estados["state"]=='SC']
sp = estados.loc[estados["state"]=='SP']
se = estados.loc[estados["state"]=='SE']
to = estados.loc[estados["state"]=='TO']

#tivemos um filtro dos dados acima, e agora está na hora de somar as mortes por estado

Sac = sum(ac['new_deaths'])
Sal = sum(al['new_deaths'])
Sap = sum(ap['new_deaths'])
Sam = sum(am['new_deaths'])
Sba = sum(ba['new_deaths'])
Sce = sum(ce['new_deaths'])
Sdf = sum(df['new_deaths'])
Ses = sum(es['new_deaths'])
Sgo = sum(go['new_deaths'])
Sma = sum(ma['new_deaths'])
Smt = sum(mt['new_deaths'])
Sms = sum(ms['new_deaths'])
Smg = sum(mg['new_deaths'])
Spa = sum(pa['new_deaths'])
Spb = sum(pb['new_deaths'])
Spr = sum(pr['new_deaths'])
Spe = sum(pe['new_deaths'])
Spi = sum(pi['new_deaths'])
Srj = sum(rj['new_deaths'])
Srn = sum(rn['new_deaths'])
Srs = sum(rs['new_deaths'])
Sro = sum(ro['new_deaths'])
Srr = sum(rr['new_deaths'])
Ssc = sum(sc['new_deaths'])
Ssp = sum(sp['new_deaths'])
Sse = sum(se['new_deaths'])
Sto = sum(to['new_deaths'])

# Acre - AC Alagoas - AL Amapá - AP Amazonas - AM Bahia - BA Ceará - CE Distrito Federal - DF Espírito Santo - ES
# Goiás - GO Maranhão - MA Mato Grosso - MT Mato Grosso do Sul - MS Minas Gerais - MG Pará - PA Paraíba - PB 
# Paraná - PR Pernambuco - PE Piauí - PI Rio de Janeiro - RJ Rio Grande do Norte - RN Rio Grande do Sul - RS 
# Rondônia - RO Roraima - RR Santa Catarina - SC São Paulo - SP Sergipe - SE Tocantins - TO

NEstados = ['Acre', 'Alagoas', 'Amapá', 'Amazonas', 'Bahia', 'Ceará', 'Distrito Federal', 'Espírito Santo', 'Goiás', 'Maranhão', 'Mato Grosso', 'Mato Grosso do Sul', 'Minas Gerais', 'Pará', 'Paraíba', 'Paraná', 'Pernambuco', 'Piauí', 'Rio de Janeiro', 'Rio Grande do Norte', 'Rio Grande do Sul', 'Rondônia', 'Roraima', 'Santa Catarina', 'São Paulo', 'Sergipe', 'Tocantins']
Mortes = [Sac, Sal, Sap, Sam, Sba, Sce, Sdf, Ses, Sgo, Sma, Smt, Sms, Smg, Spa, Spb, Spr, Spe, Spi, Srj, Srn, Srs, Sro, Srr, Ssc, Ssp, Sse, Sto]
dado = {'NAME_1': NEstados, 'Mortes': Mortes}
inform = pd.DataFrame(data=dado)

#NEstados, recebe os nomes dos estados em ordem alfabética, como estava na tabela original
#Mortes recebe as mortes por COVID-19 considerando a ordem definida em NEstados
#Cria-se um dicionário que reberá as colunas criadas e as nomeará
#Em inform, o dicionário é convertido em data frame para ser manipulado mais a frente

#Os mapas foram extraídos a partir do site:
# https://github.com/MRobalinho/GeoPandas_Brasil/tree/92c38c374c0ec3112f015e34a5148ec248390511/Shapes

# Tabelas Brasil e Estados /content/drive/My Drive/Mapa Brasil
#uf_br0 = Mapa fronteiras do Brasil
#uf_br1 = Mapa fronteiras dos estados brasileiros

uf_br0 = gpd.read_file('E:/Gabriel/Documentos/Estudos/Cruzeiro do Sul/Visualização da Informação/Projeto/Atividade Visualização-da-Informação/Exercícios .py/Covid-19/Mapa Brasil/Shapes/gadm36_BRA_0.shp')
uf_br1 = gpd.read_file('E:/Gabriel/Documentos/Estudos/Cruzeiro do Sul/Visualização da Informação/Projeto/Atividade Visualização-da-Informação/Exercícios .py/Covid-19/Mapa Brasil/Shapes/gadm36_BRA_1.shp')

#Se digitado uf_br1 mostrará as tabelas relacionadas ao mapa e ao digitar:

#uf_br1.plot(edgecolor='black', figsize=(20,8),column='NAME_1')
#Mostrará o mapa em si!

#como se trata de um mapa, é simples mostrar os dados que são relacionados 
#a ele, somente digitando o nome da variavel que contem o mapa

#Vou separar a tabela uf_br1 (Mapa) em dados que me interessam!
#Estou colocando a coluna nome, e a geometria do estado, que me interessam

MapaBrasil = uf_br1[['NAME_1','TYPE_1','geometry']]

#Plotando o gráfico MapaBrasil, mostrando que apesar de não ser a tabela original, o dados ainda são plotados
#edgecolor é a cor da borda do estado, figsize é o tamanho da imagem, 
#column definine as cores dos estados a partir de uma coluna

#MapaBrasil.plot(edgecolor='black', figsize=(20,8), column='NAME_1')

#Fiz com o método concatenação antes, mas ele deixava uma coluna NAME_1 a mais e precisaria apagar a mesma depois
#result = pd.concat([MapaBrasil, inform], axis=1, sort=False)

result = pd.merge(MapaBrasil, inform, on='NAME_1')

#Em merge eu juntei as tabelas MapaBrasil e inform, relacionando-as com a coluan NAME_1 que tem nas duas

# define uma variável que chamará a coluna que quisermos visualizar no mapa
variável = 'Mortes'

# definir o intervalo para o choropleth
vmin, vmax = 5, 5000

# criar figura e eixos para o Matplotlib
fig, ax = plt.subplots (1, figsize = (10, 6))

#Ou posso criar o mapa chamando a string ao invés da variável, ela deve ser o nome da coluna da sua tabela criada antes
#result.plot(column='Mortes', cmap='Reds', linewidth=0.8, ax=ax, edgecolor='0.5')

#Criando o mapa
result.plot(column=variável, cmap='Reds', linewidth=0.8, ax=ax, edgecolor='black')

# remova o eixo que fica em volta do mapa
ax.axis ('off')

# Adicione um título
ax.set_title ('Mortes por COVID-19 \nnos estados brasileiros', 
              fontdict = {'fontsize': '20', 'fontweight': '3'})

# criar uma anotação para a fonte de dados
ax.annotate ('Fonte: Gabriel Roberto, Dados: Brasil.io, 2020', xy = (0.1, 0.08), 
             xycoords = 'figure fraction', 
             horizontalalignment = 'left', 
             verticalalignment = 'top', 
             fontsize = 12, 
             color = '#555555')

# Criando uma barra colorida lateral para servir como legenda
sm = plt.cm.ScalarMappable(cmap='Reds', norm=plt.Normalize(vmin=vmin, vmax=vmax))

# array vazio para o intervalo de dados
sm._A = []

# adicione a barra de cores à figura
cbar = fig.colorbar(sm)

#Vamos salvar a figura em uma imagem
fig.savefig('E:\\Gabriel\\Documentos\\Estudos\\Cruzeiro do Sul\\Visualização da Informação\\Projetomap_export.png', format='png', dpi=500)