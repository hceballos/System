from tipo_cuenta import Tipo_cuenta
from query import query
import re

class Grafico():

    def generar_grafico(self, seccion, cuenta, cur):
        return {
            "header": seccion.get("header"),
            "type": seccion["tipo"],
            "title": seccion["nombre"],
            "graph_data": {
                "haxis": seccion["haxis"],
                "vaxis": seccion["vaxis"],
                "labels" : self.obtener_labels_del_grafico(seccion, cuenta, cur),
                "lines" : self.objener_lineas_del_grafico(seccion, cuenta, cur)
            }
        }

    def obtener_labels_del_grafico(self, seccion, cuenta, cur):
        if re.match('\d{1}-\d{2}-\d{2}-\d{3}', cuenta):
            sql_name_a_ejecutar = self.obtener_consulta_segun_cuenta(cuenta)
            if len(seccion['lineas']) == 0:
                return None

            linea = seccion['lineas'][0]
            return self.ejecutar_consulta_labels(linea['sql_file_path'][sql_name_a_ejecutar], cuenta, cur)
        else:
            if len(seccion['lineas']) == 0:
                return None

            linea = seccion['lineas'][0]
            return self.ejecutar_consulta_labels(linea['sql_file_path'], cuenta, cur)



    def ejecutar_consulta_labels(self, sql_file_path, cuenta, cur):
        FormatoQuery = query()
        return FormatoQuery.consulta_labels(sql_file_path, cuenta, cur)

    def objener_lineas_del_grafico(self, seccion, cuenta, cur):
        if re.match('\d{1}-\d{2}-\d{2}-\d{3}', cuenta):
            sql_name_a_ejecutar = self.obtener_consulta_segun_cuenta(cuenta)
            lineas = []
            for linea in seccion['lineas']:
                lineas.append({
                        "name" : self.obtener_name(linea['nombre']),
                        "data" : self.ejecutar_consulta_lines(linea['sql_file_path'][sql_name_a_ejecutar], cuenta, cur)
                    })
            return lineas
        else:
            lineas = []
            for linea in seccion['lineas']:
                lineas.append({
                        "name" : self.obtener_name(linea['nombre']),
                        "data" : self.ejecutar_consulta_lines(linea['sql_file_path'], cuenta, cur)
                    })
            return lineas


    def obtener_name(self, linea_nombre):
        nombre=[]
        nombre.append(linea_nombre)

        name= ''.join(nombre)
        return name

    def obtener_consulta_segun_cuenta(self, cuenta):
        FormatoVariable = Tipo_cuenta()
        return FormatoVariable.consulta_segun_cuentas(cuenta)

    def ejecutar_consulta_lines(self, sql_file_path, cuenta, cur):
        FormatoQuery = query()
        return FormatoQuery.consulta_lines(sql_file_path, cuenta, cur)
