from tipo_cuenta import Tipo_cuenta
from query import query
import re

class Tendencia():

    def generar_tendencia(self, seccion, cuenta, cur):
        # si la variable tiene el patron de una cuentra, entonces aplicar la consulta segun tipo de cuenta
        if re.match('\d{1}-\d{2}-\d{2}-\d{3}', cuenta):
            query_result = None
            sql_name_a_ejecutar = self.obtener_consulta_segun_cuenta(cuenta)
            query_result = self.ejecutar_consulta_desde_archivo(seccion['sql_file_path'][sql_name_a_ejecutar], cuenta, cur)
        else:
            query_result = None
            query_result = self.ejecutar_consulta_desde_archivo(seccion['sql_file_path'], cuenta, cur)

        return {
            "header": seccion.get("header"),
            "type": seccion["tipo"],
            "title": seccion["nombre"],
            "table_object": {
                "table_data": query_result
            }
        }

    def obtener_consulta_segun_cuenta(self, cuenta):
        FormatoVariable = Tipo_cuenta()
        return FormatoVariable.consulta_segun_cuentas(cuenta)

    def ejecutar_consulta_desde_archivo(self, sql_file_path, cuenta, cur):
        FormatoQuery = query()
        return FormatoQuery.ejecutar_consulta_Tendencia(sql_file_path, cuenta, cur)