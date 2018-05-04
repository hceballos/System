from tipo_cuenta import Tipo_cuenta
from query import query
import json
import re

class Gauge():

    def generar_gauge(self, seccion, cuenta, cur):
        return {
            "header": seccion.get("header"),
            "type": seccion["tipo"],
            "title": seccion["nombre"],
            "table_data": self.ejecutar_consulta_desde_archivo_gauge(seccion['sql_file_path'], cuenta, cur),
            # json.dumps() para sacar el unicode u'string'
            "options": json.dumps(seccion['options']),
            "table_object": {
                "table_header": seccion['table_metadata']['column_names'],
                "table_styles": {
                    "columns": seccion['table_metadata']['styles']['columns']
                }
            }
        }

    def ejecutar_consulta_desde_archivo_gauge(self, sql_file_path, cuenta, cur):
        FormatoQuery = query()
        return FormatoQuery.ejecutar_consulta_gauge(sql_file_path, cuenta, cur)