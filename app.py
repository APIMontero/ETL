# Importar modulos para trabajar con planillas de cálculo, csv y texto. Incluir del sistema y JSON
import csv
import json
import pandas as pd

# Constantes y variables
extensiones = [
    dict(id=0, tipo="csv"),
    dict(id=1, tipo="json"),
    dict(id=2, tipo="txt"),
    dict(id=3, tipo="xls")  #, y asi sucesivamente
]


# Sub procesos, funciones y lambdas
def extensiones_permitidas(extensions: list):
    print(f"Tipos de archivos permitidos:")
    for extension in extensions:
        print(f'{int(extension["id"]) + 1}. {extension["tipo"]}')

def xls_to_csv():
    pass

def xls_to_json():
    pass

def csv_to_xls():
    pass

def json_to_xls():
    pass


def csv_to_json(ruta_csv, ruta_json):
    # create a dictionary
    data = {}

    # Open a csv reader called DictReader
    with open(ruta_csv, encoding='utf-8') as csvf:
        csv_reader = csv.DictReader(csvf)

        # Convert each row into a dictionary
        # and add it to data
        for rows in csv_reader:
            # Assuming a column named 'No' to
            # be the primary key
            key = rows['id']
            data[key] = rows

    # Open a json writer, and use the json.dumps()
    # function to dump data
    with open(ruta_json, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))


def json_to_csv(ruta_json, ruta_csv):
    """
        Step 1: To convert JSON files to CSV, you first need to import Pandas Library in Python.
        OK -> see: import pandas as pd ...
        Step 2: Load the JSON data into Pandas DataFrame.
    """
    data = pd.read_json(ruta_json)
    # Step 3: Write the data to CSV file.
    data.transpose().to_csv(ruta_csv, index=False)
    # data.to_csv(ruta_csv, index=True)


def procesar_archivo(ruta: str, tipo_inicial: int, tipo_final: int):
    if tipo_final == 1 and tipo_inicial == 0:  # conversion a JSON
        ruta_sin_extension = ruta[:-4:]
        csv_to_json(ruta, ruta_json=f"{ruta_sin_extension}.json")
        print(f'Estado actual: {ruta} convertida a JSON y dejada en {ruta_sin_extension + ".json"}.')
    elif tipo_final == 0 and tipo_inicial == 1:  # conversion a JSON
        ruta_sin_extension = ruta[:-5:]
        # print(ruta_sin_extension)
        json_to_csv(ruta_json=ruta, ruta_csv=f"{ruta_sin_extension + '2'}.csv")
        print(f'Estado actual: {ruta} convertida a CSV y dejada en {ruta_sin_extension + "2.csv"}.')
    else:
        print("Tipo de archivo no permitido.")


# Proceso principal
def main():
    extensiones_permitidas(extensions=extensiones)
    procesar_archivo("tmp/archivo.csv", tipo_inicial=0, tipo_final=1)
    procesar_archivo("tmp/archivo.json", tipo_inicial=1, tipo_final=0)


# Llamada desde la condicional del script
if __name__ == "__main__":
    main()
