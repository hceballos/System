from tipo_cuenta import Tipo_cuenta
from query import query
import re

class Tabla():


    def generar_tabla(self, seccion, cuenta, cur):
        # si el patron de la variable es una cuenta, entonces asignar el tipo de consulta:
        if re.match('\d{1}-\d{2}-\d{2}-\d{3}', cuenta):

            query_result = None
            if isinstance(seccion['sql_file_path'], basestring):
                query_result = self.ejecutar_consulta_desde_archivo(seccion['sql_file_path'], cuenta, cur)
            elif isinstance(seccion['sql_file_path'], dict):
                sql_name_a_ejecutar = self.obtener_consulta_segun_cuenta(cuenta)
                query_result = self.ejecutar_consulta_desde_archivo(seccion['sql_file_path'][sql_name_a_ejecutar], cuenta, cur)
        else:

            if isinstance(seccion['sql_file_path'], basestring):
                query_result = self.ejecutar_consulta_desde_archivo(seccion['sql_file_path'], cuenta, cur)
            elif isinstance(seccion['sql_file_path'], dict):
                query_result = self.ejecutar_consulta_desde_archivo(seccion['sql_file_path'], cuenta, cur)


        return {
            "header": seccion.get("header"),
            "type": seccion["tipo"],
            "title": seccion["nombre"],
            "table_object": {
                "table_header": seccion['table_metadata']['column_names'],
                "table_data": query_result['data'],
                "table_styles": {
                    "columns": seccion['table_metadata']['styles']['columns']
                }
            }
        }

    def obtener_consulta_segun_cuenta(self, cuenta):
        FormatoVariable = Tipo_cuenta()
        return FormatoVariable.consulta_segun_cuentas(cuenta)

    def ejecutar_consulta_desde_archivo(self, sql_file_path, cuenta, cur):
        FormatoQuery = query()
        return FormatoQuery.ejecutar_consulta(sql_file_path, cuenta, cur)