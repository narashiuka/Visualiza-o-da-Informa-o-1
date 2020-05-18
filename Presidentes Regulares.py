#Importamos todas tabela que serão usados 

import matplotlib.pyplot as plt; plt.rcdefaults() 
import numpy as np 
import pandas as pd 
import seaborn as sns
import plotly.graph_objects as go

from pandas import read_csv

#O arquivo foi retirado do site: https://github.com/gabrielzanlorenssi/presidential_approval/blob/master/aprovacao.csv

presidentes = pd.read_csv("E:/Gabriel/Documentos/Estudos/Cruzeiro do Sul/Visualização da Informação/Projeto/Atividade Visualização-da-Informação/Exercícios .py/Presidentes/aprovacao.csv") 
presidentes = presidentes.fillna(0)

#Neste passo estamos pegando os dados de um csv chamado aprovacao e colocando dentro da tabela presidentes
#fillna irá avaliar os dados que tiverem NA em sua composição e irá substitui-los por 0

#Neste passo abaixo, iremos criar matrizes de uma coluna que contém os dados de votação separados

lider = presidentes["presidente"]
ru = presidentes["ruim"]
reg = presidentes["regular"]
ot = presidentes["otimo_bom"]

#A variavel number cria um arranjo que terá o tamanho da tabela lider, que será usado mais a frente

number = np.arange(len(lider)) 

#Iremos filtrar os dados e faremos tabelas para cada presidente
#para facilitar cálculos, e o filtro ocorre graças ao comando loc

Temer = presidentes.loc[presidentes["presidente"]=="TEMER"]
Dilma = presidentes.loc[presidentes["presidente"]=="DILMA"]
Lula = presidentes.loc[presidentes["presidente"]=="LULA"]
Sarney = presidentes.loc[presidentes["presidente"]=="SARNEY"]
Collor = presidentes.loc[presidentes["presidente"]=="COLLOR"]
Itamar = presidentes.loc[presidentes["presidente"]=="ITAMAR"]
FHC = presidentes.loc[presidentes["presidente"]=="FHC"]

#Depois que o filtro foi realizado, agora é a hora de calcular a soma da coluna "regular"
#de cada presidente, sabendo assim quando votos cada um teve, respectivos a esse dado, no caso "regular"

RTotal = sum(presidentes["regular"])
#Claro também precisamos saber quantos votos "regular" foram realizados para sabermos a proporção de cada presidente

RTemer = sum(Temer["regular"])
RDilma = sum(Dilma["regular"])
RLula = sum(Lula["regular"])
RSarney = sum(Sarney["regular"])
RCollor = sum(Collor["regular"])
RItamar = sum(Itamar["regular"])
RFHC = sum(FHC["regular"])

marcas = ['Temer','Dilma','Collor','Lula','Sarney','Itamar','FHC']
regular = [RTemer*100/RTotal, RDilma*100/RTotal, RCollor*100/RTotal, RLula*100/RTotal, RSarney*100/RTotal, RItamar*100/RTotal, RFHC*100/RTotal]
colors=["blue", "red", "yellow", "green", "pink", "brown", "grey"]

#Marcas recebe os nomes dos presidentes em ordem que definirá a apresentação dos dados mais a frente
#Em regular é calculado a proporção de votos "regular" de cada presidente e criada uma lista
#Colors já define as cores respectivas de cada presidente para uso de um gráfico

plt.pie(regular, labels=marcas, colors=colors, autopct="%1.f%%", shadow=False, startangle=45) 
plt.title('Presidentes Mais Regulares') 

#plt.pie diz que será criado um gráfico de pizza, trazendo a variavel regular como seu dado,
#labels receberá o nome dos presidentes para servir como título das fatias
#colors recebe as cores dos respectivos presidentes
#autopct define as casas decimais que serão apresentadas no gráfico
#shadow false diz que não haverá uma sombra abaixo da pizza, deixando mais legível o gráfico neste caso
#startangle define o ângulo que o gráfico irá iniciar

plt.show()