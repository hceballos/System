import argparse

import shutil
from lib.CSVReader import CSVReader
from lib.MovementsDB import MovementsDB
from lib.ManufacturerYearQuery import ManufacturerYearQuery
from lib.InputProcessor import InputProcessor
from lib.InputCCostos import InputCCostos
from lib.InputAdo import InputAdo
from lib.InputComplemento import InputComplemento
from jinja2 import Environment, FileSystemLoader
from lib.distribucion import Distribucion


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("--main", help="Genera la base de datos.")
    parser.add_argument("--cuentas", help="Analisis de cuentas")
    parser.add_argument("--ruts", help="Analisis de ruts")
    parser.add_argument("--gg", help="Analisis de cuentas, 1 informe por cada cuenta.")
    parser.add_argument("--rutInvalidos", help="Observaciones en digitacion de ruts.")
    parser.add_argument("--operation", help="operation", choices=["main", "cuentas", "ruts", "gg", "rutInvalidos"])
    args = parser.parse_args()

    print "Processing: ", args.operation

    FILE_DB = 'data.db'
    FOLDER_INPUT = 'input/input_Mayores/'
    FOLDER_CSV = 'csv/'



    db_file_path = 'data.db'
    secciones_json_path_cuentas = 'input/JefeContable.json'

    cuentas_sql_path  = 'sql/cuentas/Cuentas.sql'
    secciones_json_path_ruts  = 'input/JefeContableRuts.json'
    ruts_sql_path  = 'sql/ruts/ruts.sql'

    secciones_json_path_GerenteGeneral  = 'input/GerenteGeneral.json'

    #Nota : python main.py --operation main
    if args.operation == 'main':
        shutil.rmtree('csv')
        inputProcessor = InputProcessor()
        inputProcessor.setInputFolder(FOLDER_INPUT)
        inputProcessor.setCSVFolder(FOLDER_CSV)
        inputProcessor.process()
        reader = CSVReader(FOLDER_CSV)
        db = MovementsDB(FILE_DB)
        db.saveRegisters(reader.registers)
        InputCCostos = InputCCostos(FILE_DB)
        InputAdo = InputAdo(FILE_DB)
        InputComplemento = InputComplemento(FILE_DB)

    elif args.operation == 'cuentas':
        Dist= Distribucion(secciones_json_path_cuentas, db_file_path, cuentas_sql_path)
        Dist.inicio()

    elif args.operation == 'ruts':
        Dist= Distribucion(secciones_json_path_ruts, db_file_path, ruts_sql_path)
        Dist.inicio()

    elif args.operation == 'gg':
        Dist= Distribucion(secciones_json_path_GerenteGeneral, db_file_path, cuentas_sql_path)
        Dist.inicio()


    else:
        print ("operacion no soportada")

    print ("Listo ")

