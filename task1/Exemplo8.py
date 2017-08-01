#%matplotlib inline
import pandas as pd
import pymssql
import matplotlib.pyplot as plot
from common import DBConnection
from common import configuration
from task1 import querys

dbc = DBConnection(configuration.confSQLSERVER["host"], configuration.confSQLSERVER["database"],
                   configuration.confSQLSERVER["user"], configuration.confSQLSERVER["password"])
#print(dbc)
sql = querys.sql1

dados = pd.read_sql(sql, dbc.getconnection())
dbc.closeconnection()

#qtd1 = df['mesanocompetencia'].value_counts()

graph = pd.crosstab(index=dados['mesanocompetencia'],columns=dados['instrumento']).apply(lambda r: r/r.sum() *100,axis=1)
graph = pd.crosstab(dados['mesanocompetencia'],dados['instrumento'])
graph.plot(kind='bar', figsize=(200,60), grid=True, rot=0, legend=False)
plot.title('Quantidade de atendimetos por mês em 2017')
plot.xlabel('Quantidade de atendimentos')
plot.show()