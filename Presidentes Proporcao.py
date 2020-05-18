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

#Dentro de três variáveis somamos os dados de matrizes que criamos acima, 
#cada variavel pega a soma dos votos recebidos por tipo

votoOt = sum(ot)
votoReg = sum(reg)
votoRu = sum(ru)

votos = votoOt + votoReg + votoRu
#Criamos uma variavel que pega toda aquela soma dos votos 

pesquisa = ["Votos Bons", "Votos Regulares", "Votos Ruins"]
proporcao = [votoOt*100/votos, votoReg*100/votos, votoRu*100/votos]
cont = np.arange(len(proporcao)) 

#Foi criada uma variável pesquisa que receberá o título dos tipos de votos
#Proporcao recebe a a proporção dos votos que foram realizados, também por tipo
#cont recebe um arranjo no tamanho da lista proporcao

#Criaremos um gráfico de barras (coluna), 
#que receberá cont como tamanho dos dados, proporcao como 'y'
#Receberá também as cores de cada coluna, verde, amarelo e vermelho

#Xticks recebe os dados da variável x que no caso será pesquisa, e colocaremos nenhuma rotação no titulo das colunas
#Ylabel é definido como título das colunas em y
#Title define o título do gráfico que ficará logo em cima dele

plt.bar(cont, proporcao, color=['green', 'yellow', 'red']) 
plt.xticks(cont, pesquisa, rotation=0) 
plt.subplots_adjust(right = 2)
plt.ylabel('Votação de Popularidade') 
plt.title('Proporção dos votos de Pesquisa ao redor do anos') 
 
plt.show() 