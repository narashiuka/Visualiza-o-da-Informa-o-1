#Anteriormente foi instalada a biblioteca GeoPandas que será usada para plotar um gráfico logo mais
#Importamos todas tabela que serão usados 

import matplotlib.pyplot as plt; plt.rcdefaults() 
import numpy as np 
import pandas as pd 
#import plotly.graph_objects as go
#import geopandas as gpd

from pandas import read_csv

#Puxamos os dados sobre Game of Thrones da tabela character-predictions, que foi retirada do site
#https://www.kaggle.com/mylesoneill/game-of-thrones

game = pd.read_csv("E:/Gabriel/Documentos/Estudos/Cruzeiro do Sul/Visualização da Informação/Projeto/'Atividade Visualização-da-Informação'/character-predictions.csv") 

#Já separamos em variaveis os nomes dos personagens e sua popularidade
#Indice recebe um arranjo do tamanho da variavel nomes

names = game["name"]
popularidade = game["popularity"]
indice = np.arange(len(names)) 

#iremos filtrar a tabela original para receber somente os dados em que a popularidade seja acima de 70%
#importante frisar que nesta pesquisa os participantes escolhiam os seus personagens preferidos
#não tendo um limite de escolha, por isto alguns personagens terão popularidade total

gamefiltrado = game.loc[game["popularity"]>0.7]

gamefiltrado = gamefiltrado.fillna(0)

#Os dados que forem Na na tabela serão substituidos por 0 utilizando a função fillna

pop = list(gamefiltrado["popularity"]*100)
nome = list(gamefiltrado["name"])
ind = np.arange(len(nome)) 

#A função list transforma as variaveis em lista, isso é necessário para a criação do gráfico de barras
#Definiremos que pop receberá a popularidade dos personagens multiplicado por 100 para se transformar em porcentagem
#nome receberá os nomes que estão na tabela que foi filtrada
#ind receberá um arranjo que terá o tamanho da variavel nome

#Plt.bar cria o gráfico de barras
#ind será o tamanho dos dados que serão anexados ao gráfico
#pop será o dado 'y' que será aplicado ao gráfico
#nome será o dado 'x' que será aplicado ao gráfico
#"color" reberá uma paleta de cores que estarão próximas do vermelho
#rotation girá os nomes das colunas 90° para ficarem mais legíveis
#ylabel será o título das colunas no lado esquerdo, pode-se usar xlabel também
#title será os título do gráfico, logo acima dele

plt.bar(ind, pop, color=sns.color_palette("Reds")) 
plt.xticks(ind, nome, rotation=90) 
plt.subplots_adjust(right = 2)
plt.ylabel('Popularidade') 
plt.title('Mais Populares em Game of Thrones') 
 
plt.show() 
