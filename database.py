from mysql import connector

from settings import USER, PASSWORD, HOST, DATABASE


class SQLConnect(object):

    def __init__(self):
        self._conn = None

    def get_connection(self):
        self._conn = connector.connect(user=USER, password=PASSWORD, host=HOST, database=DATABASE)

    def execute_query(self, query):
        """"""
        try:
            cursor = self._conn.cursor()
        except:
            return None
        else:
            return cursor.execute(query)
        finally:
            if cursor:
                cursor.close()
                self._conn = None






