from contabilidad import Contabilidad
from tabla import Tabla
from grafico import Grafico
from tendencia import Tendencia
from render import Render
from gauge import Gauge


class Distribucion(Contabilidad):
    def __init__(self, secciones_json_path, db_file_path, cuentas_sql_path):
        Contabilidad.__init__(self, secciones_json_path, db_file_path, cuentas_sql_path)

    def inicio(self):
        for cuenta in self.cuentas:
            render_data = []
            for seccion in self.secciones:
                render_data.append(
                    self.generar_render_data(seccion, cuenta, self.cur)
                )

            print "Rendering report for : " + cuenta
            Rendering = Render()
            Rendering.renderHtml(render_data, cuenta, self.secciones[0]['sql_file_path'])


    def generar_render_data(self, seccion, cuenta, cur):
        tipo = seccion['tipo']

        if tipo == 'tabla':
            FormatoTabla = Tabla()
            return FormatoTabla.generar_tabla(seccion, cuenta, cur)

        elif tipo == 'grafico':
            FormatoGrafico = Grafico()
            return FormatoGrafico.generar_grafico(seccion, cuenta, cur)

        elif tipo == 'tendencia':
            FormatoTendencia = Tendencia()
            return FormatoTendencia.generar_tendencia(seccion, cuenta, cur)

        elif tipo == 'gauge':
            FormatoGauge = Gauge()
            return FormatoGauge.generar_gauge(seccion, cuenta, cur)