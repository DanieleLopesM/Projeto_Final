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

#%% Gerando estatísticas descritivas

# Tabela de estatísticas descritivas para variáveis quantitativas

descritivas = df2[['ghi', 'ano']]

descritivas.describe()



#Características das variáveis do dataset
df2.info()

#%%

import matplotlib
print('matplotlib: {}'.format(matplotlib.__version__))


#%%

# Iniciando com o gráfico básico (scatterplot)
# Neste caso, devemos especificar as variáveis dos eixos x e y no

sns.scatterplot(df2, x="ano", y="ghi")

#%%

# vamos implementar o seguinte gráfico
# Note que vamos separar cada temperatura por meio da cor do gráfico

sns.lineplot(df2, x="ano", y="ghi", hue="temperatura")

#%%

# Vamos formatar um pouco mais o gráfico

sns.lineplot(df2, x="ano", y="ghi", hue="temperatura", marker="o")

plt.title("Radiação")
plt.xlabel('ano',fontsize=12)
plt.ylabel('energia',fontsize=12)
plt.legend(title='temperatura')
plt.show()


#%% Gráfico de Calor

# Vamos gerar um gráfico de calor que distingue informações por meio de cores
# O banco de dados contém informações sobre o tempo para chegar à escola
# Fonte: Fávero & Belfiore (2017, Capítulo 12)

ano_ghi = pd.read_csv("dadosR.csv")


#%%

# Inicialmente, vamos selecionar as variáveis quantitativas do banco de dados

df2 = ano_ghi[['ano','ghi','temperatura']]

# Vamos trabalhar o gráfico de calor no contexto das correlações entre variáveis
# Portanto, primeiramente, vamos criar a matriz de correlações (função "cor")
# Lembrando: selecionar apenas as variáveis quantitativas da base de dados

corr = ano_ghi.corr()
#%%

# Agora vamos elaborar um gráfico de calor (heatmap) com algumas formatações

sns.heatmap(corr, center=0)
