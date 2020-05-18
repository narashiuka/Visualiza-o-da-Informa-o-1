#Anteriormente foi instalada a biblioteca GeoPandas que será usada para plotar um gráfico logo mais
#Importamos todas tabela que serão usados 

import matplotlib.pyplot as plt; plt.rcdefaults() 
import numpy as np 
import pandas as pd 
import seaborn as sns
import plotly.graph_objects as go
import geopandas as gpd

from pandas import read_csv

covid = pd.read_csv("E:/Gabriel/Documentos/Estudos/Cruzeiro do Sul/Visualização da Informação/Projeto/Atividade Visualização-da-Informação/Exercícios .py/Covid-19/covid19.csv")

#Dados retirados do site:
#https://brasil.io/dataset/covid19/caso_full/?page=3
#usando a tabela "covid19-8369e44a27c245e6892c18cf1606b3ec"

#Neste passo, iremos filtrar os dados, trazendo para seus respectivos estados uma 
#tabela contendo seus dados separados, facilitando assim uma manipulação mais a frente

estados = covid.loc[covid["place_type"]=='state']

sp = estados.loc[estados["state"]=='SP']
k = {'Data': sp['date'], 'Confirmados': sp['new_confirmed']}

#Os dados de São Paulo foram filtrados e transformados em dicionários, logo em seguida, se tornaram um data frame

diario = pd.DataFrame(k)
print(diario)

#plt.plot(x, y, cor)
#xticks(rotation) está servindo para rotacionar os titulos de coluna do eixo x, para melhor visualiza-los
#ax = plt.gca() e ax.invert_xaxis() juntos invertem o eixo x que será apresentado de forma melhor
#plt.rcParams['figure.figsize'] = (20,10) define o tamanho da imagem

plt.plot(diario['Data'], diario['Confirmados'], 'r')
plt.xticks(rotation=90)
ax = plt.gca()
ax.invert_xaxis()
plt.rcParams['figure.figsize'] = (30,10)
plt.title('Casos confirmados de Covid em São Paulo', loc='center', fontsize=22, fontweight=30) 
plt.ylabel('Mortes', {'color': 'black', 'fontsize': 20}) 
plt.show() 
