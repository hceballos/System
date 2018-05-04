import re
from jinja2 import Environment, FileSystemLoader

class Render():


    def renderHtml(self, render_data, cuenta, file_path):
        #separar secciones que sean headers
        sections = []
        header_elements = []
        for x in render_data:
            if x["header"] == True:
                header_elements.append(x)
            else:
                sections.append(x)

        env = Environment(
        loader=FileSystemLoader('templates')

        )

        if re.match('sql\/GGeneral', file_path):
            template = env.get_template('GerenteGeneral.html')
            Html_file = open("output/GerenteGeneral/AnalisisCuenta.html", "wb")

        elif re.match('sql\/ruts', file_path):
            template = env.get_template('Auxiliares.html')
            Html_file = open("output/JefeContable/Auxiliares/"+str(cuenta)+".html", "wb")

        elif re.match('sql\/cuentas', file_path):
            template = env.get_template('JefeContable.html')
            Html_file = open("output/JefeContable/AnalisisCuenta/"+str(cuenta)+".html", "wb")

        Html_file.write(
        template.render(
            header_elements = header_elements,
            sections = sections
         )
        )