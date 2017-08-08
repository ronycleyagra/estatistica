sqloficinapalestra = "select distinct(codrealizacao) as qtdrealizacoes, month(mesanocompetencia) as mes, instrumento from " \
       "historicorealizacoescliente where instrumento like '%oficina%' or instrumento like '%palestra%';"

sqlpalestras = "select distinct(codrealizacao) as qtdrealizacoes, month(mesanocompetencia) as mes, instrumento from " \
       "historicorealizacoescliente where instrumento like '%palestra%';"

sqloficinas = "select distinct(codrealizacao) as qtdrealizacoes, month(mesanocompetencia) as mes, instrumento from " \
       "historicorealizacoescliente where instrumento like '%oficina%';"

sqlcursos = "select distinct(codrealizacao) as qtdrealizacoes, month(mesanocompetencia) as mes, instrumento from " \
       "historicorealizacoescliente where instrumento like '%cursos pre%';"

sqlseminarios = "select distinct(codrealizacao) as qtdrealizacoes, month(mesanocompetencia) as mes, instrumento from " \
       "historicorealizacoescliente where instrumento like '%seminario%';"

sqlworkshops = "select distinct(codrealizacao) as qtdrealizacoes, month(mesanocompetencia) as mes, instrumento from " \
       "historicorealizacoescliente where instrumento like '%workshop%';"