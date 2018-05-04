import sqlite3
import json

class Contabilidad(object):
    def __init__(self, secciones_json_path, db_file_path, cuentas_sql_path):
        self.secciones_json_path = secciones_json_path
        self.db_file_path = db_file_path
        self.cuentas_sql_path = cuentas_sql_path

        self.read_secciones_json(secciones_json_path)
        self.sql_connect(db_file_path)
        self.read_Cuentas(cuentas_sql_path)

    def read_secciones_json(self, secciones_json_path):
        with open(secciones_json_path) as secciones_json:
            self.secciones = json.load(secciones_json)

    def sql_connect(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.conn.text_factory = str
        self.cur = self.conn.cursor()

    def read_Cuentas(self, cuentas_sql_path):
        with open(cuentas_sql_path) as sql_file:
            sql_query = sql_file.read()

            registros = []
            variable = self.cur.execute(sql_query)
            for row in variable:
                registros.append(list(row))

            self.cuentas = [x[0] for x in registros]