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
    
df_solar = pd.read_csv('solar_weather.csv', delimiter=',')
df_solar

#Características das variáveis do dataset
df_solar.info()

#Estatísticas univariadas
df_solar.describe()

