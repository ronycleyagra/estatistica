import pymssql

'''
    Documentação.
'''
class DBConnection(object):

    def __init__(self, host, database, user, password):
        self.__host = host
        self.__database = database
        self.__user = user
        self.__password = password
        self.__con = ""

    def getconnection(self) -> pymssql.Connection:
        self.con = pymssql.connect(host=self.__host, database=self.__database, user=self.__user, password=self.__password)
        return self.con

    def closeconnection(self):
        self.con.close

    def __str__(self):
        return "host: " + self.__host + ", database: " + self.__database + ", user: " + self.__user + ", password: " + self.__password