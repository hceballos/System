import re

class Tipo_cuenta():

    def consulta_segun_cuentas(self, cuenta):
        if re.match('^\s*1', cuenta):
            return "activo"
        if re.match('^\s*2', cuenta):
            return "pasivo"
        if re.match('^\s*3', cuenta):
            return "patrimonio"
        if re.match('^\s*4', cuenta):
            return "ingresos"
        if re.match('^\s*5', cuenta):
            return "egresos"
        if re.match('^\s*6', cuenta):
            return "impuestos"
        if re.match('^\s*7', cuenta):
            return "derechos"
        if re.match('^\s*8', cuenta):
            return "responsabilidad"
        if re.match('^\s*9', cuenta):
            return "orden"
        raise Exception("Tipo de cuenta no encontrado: {}".format(cuenta))