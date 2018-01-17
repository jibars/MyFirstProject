import psycopg2
class DataBaseError(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje

    def __str__(self):
        return self.mensaje

class postgres_repository:
    def __init__(self, host, port, user, database, password):
        self.host = host
        self.port = port
        self.user = user
        self.database = database
        self.password = password
        self.conn = None
        self.cur = None

    def connect(self):
        self.conn = psycopg2.connect(host = self.host, port = self.port, user = self.user, database = self.database, password = self.password)
        self.cur = self.conn.cursor()
        return self

    def transaction(self, sql):
        try:
            self.cur.execute(sql)
            self.conn.commit()
        except:
            self.conn.rollback()
            raise DataBaseError("Transaction error. Rollback")

    def create(self, sql):
        self.transaction(sql)

    def get(self, sql):
        self.cur.execute(sql)
        return self.cur.fetchall()


    def post(self, sql):
        self.transaction(sql)

    def delete(self, sql):
        self.transaction(sql)

    def close(self):
        self.cur.close
        self.conn.close()
