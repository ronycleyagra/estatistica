#%matplotlib inline
import pandas as pd
import pymssql
import matplotlib.pyplot as plot
from common.DBConnection import DBConnection
from task1 import querys

def plotgraph(resultset, name):

       df = pd.crosstab(resultset['mes'], resultset['instrumento'])
       df.plot(kind='bar', figsize=(15, 4.5), grid=True, rot=0, legend=True,
                  title='Quantidade de atendimetos em '+name+' por mês em 2017')

       plot.savefig('/home/rony/PycharmProjects/estatistica/task1/graphs/'+name+'.jpg',
                    dpi='figure', facecolor='w',
                    edgecolor='w',orientation='portrait',
                    papertype=None, format=None,
                    transparent=False, bbox_inches=None,
                    pad_inches=0.1, frameon=None)

dbc = DBConnection()

dados = pd.read_sql(querys.sqlpalestras, dbc.getconnection())
plotgraph(dados,"palestras")

dados = pd.read_sql(querys.sqloficinas, dbc.getconnection())
plotgraph(dados,"oficinas")

dados = pd.read_sql(querys.sqlcursos, dbc.getconnection())
plotgraph(dados,"cursos")

dados = pd.read_sql(querys.sqlseminarios, dbc.getconnection())
plotgraph(dados,"seminarios")

#dados = pd.read_sql(querys.sqlworkshops, dbc.getconnection())
#plotgrapf(dados,"workshops")

dbc.closeconnection()