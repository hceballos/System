import re

class query():

    def ejecutar_consulta(self, sql_file_path, cuenta, cur):
        with open(sql_file_path) as sql_file:
            sql_query = sql_file.read()

            if re.match('sql\/GGeneral', sql_file_path):
                cursor = cur.execute(sql_query)

            elif re.match('sql\/cuentas', sql_file_path):
                cursor = cur.execute(sql_query, (cuenta,))

            elif re.match('sql\/ruts', sql_file_path):
                cursor = cur.execute(sql_query, (cuenta,))

            result_list = cursor.fetchall()

            result = []
            for tupla in result_list:
                t = []
                for valor in tupla:
                    t.append(self._agregar_puntos_decimales_si_es_que_es_un_numero(valor))
                result.append(t)

            column_names = [i[0] for i in cursor.description]

        return {
            "headers": column_names,
            "data": result
        }

    def _agregar_puntos_decimales_si_es_que_es_un_numero(self, valor):
        if isinstance(valor, int):
            return ('{:,}'.format(int(valor)).replace(',', '.'))
        return valor


    def consulta_labels(self, sql_file_path, cuenta, cur):
        with open(sql_file_path) as sql_file:
            sql_query = sql_file.read()

            cursor = cur.execute(sql_query, (cuenta,))
            result_list = cursor.fetchall()
            return [i[0] for i in cursor.description[1:]]

    def consulta_lines(self, sql_file_path, cuenta, cur):
        with open(sql_file_path) as sql_file:
            sql_query = sql_file.read()

            cursor = cur.execute(sql_query, (cuenta,))
            result_list = cursor.fetchall()
            column_names = [i[0] for i in cursor.description]
            data= [list(i) for i in result_list]
            return self.eldata(data)

    def eldata(self, data):
            for elemento in data:
                return elemento[1:]

    def ejecutar_consulta_Tendencia(self, sql_file_path, cuenta, cur):
        with open(sql_file_path) as sql_file:
            sql_query = sql_file.read()

            cursor = cur.execute(sql_query, (cuenta,))
            datos=[]
            for row in cursor:
                datos.append(list(row))

            column_names = [i[0] for i in cursor.description]

            return [column_names] + datos

    def ejecutar_consulta_gauge(self, sql_file_path, cuenta, cur):
        with open(sql_file_path) as sql_file:
            sql_query = sql_file.read()

            cursor = cur.execute(sql_query)
            result_list = cursor.fetchall()
            column_names = [i[0] for i in cursor.description]
            data= [list(i) for i in result_list]
            return column_names + list(i)