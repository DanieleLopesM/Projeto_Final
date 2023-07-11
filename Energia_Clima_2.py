# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 20:42:28 2023

@author: Eliane Pilan
"""

# In[ ]: Importação dos pacotes necessários
    
import pandas as pd # manipulação de dado em formato de dataframe
import seaborn as sns # biblioteca de visualização de informações estatísticas
import matplotlib.pyplot as plt # biblioteca de visualização de dados
import statsmodels.api as sm # biblioteca de modelagem estatística
import numpy as np # biblioteca para operações matemáticas multidimensionais
from statsmodels.iolib.summary2 import summary_col # comparação entre modelos
import plotly.graph_objs as go # gráfico 3D
from scipy.stats import pearsonr # correlações de Pearson
from sklearn.preprocessing import LabelEncoder # transformação de dados

# In[ ]:
    
df_solar = pd.read_csv('dadosR.csv', delimiter =',')
df_solar

#selecionar somente mes Janeiro

df2 = df_solar.query('mes == 1')

#Estatísticas univariadas
df2.describe()

#Características das variáveis do dataset
df2.info()

#%% Histograma - continuar grafico

# A seguir, vamos elaborar o histograma de energia radiação  (GHI)
# O banco de dados é o mesmo que já utilizamos anteriormente

# Iniciando com o gráfico básico utilizando o próprio pandas dataframe com o método "hist"

df2['ghi'].hist(bins=5)


#%%

# Na forma por categoria dos pontos ("style")

sns.scatterplot(data=atlas_ambiental, x="ghi", y="ano", size="idade", hue="color", style="style")
plt.title("Indicadores dos Distritos do Município de São Paulo")
plt.xlabel('Renda',fontsize=12)
plt.ylabel('Escolaridade',fontsize=12)
plt.show()

