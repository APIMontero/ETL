# Importar modulos para trabajar con planillas de cálculo, csv y texto. Incluir del sistema y JSON
import csv
import json
# Constantes y variables
extensiones = [
    dict(id=0,tipo="csv"),
    dict(id=1,tipo="json"),
    dict(id=2,tipo="txt"),
    dict(id=3,tipo="xls")  #, y asi sucesivamente
]
# Sub procesos, funciones y lambdas
def extensiones_permitidas(extensions:list):
    print(f"Tipos de archivos permitidos:")
    for extension in extensions:
        print(f'{int(extension["id"]) + 1}. {extension["tipo"]}')


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


# Proceso principal

# Llamada desde la condicional del script
def procesar_archivo(ruta:str,tipo_inicial:int, tipo_final:int):
    if tipo_final == 1 and tipo_inicial == 0:  # conversion a JSON
        ruta_sin_extension = ruta[:-4:]
        csv_to_json(ruta, ruta_json=f"{ruta_sin_extension}.json")
        print(f'Estado actual: {ruta} convertida a JSON y dejada en {ruta[:-4:]+".json"}.')
    else:
        print("Tipo de archivo no permitido.")

def main():
    extensiones_permitidas(extensions=extensiones)
    procesar_archivo("tmp/archivo.csv",tipo_inicial=0, tipo_final=1)


if __name__ == "__main__":
    main()
