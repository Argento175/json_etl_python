# JSON ETL [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

import json


def serializar():
    print("Funcion que genera un archivo JSON")
    # JSON Serialize
    # Armar un JSON que represente los datos personales
    # de su persona (puede inventar los datos sino quiere exponer
    # información confidencial)

    # Debe armar un JSON que tenga como datos
    # nombre, apellido, DNI
    # Dentro debe tener una lista donde coloque cantidad de elementos de vestir
    # ejemplo -->
    #  { "prenda": "zapatilla", "cantidad": 4 }
    #  { "prenda": "remeras", "cantidad": 12 }
    # Que su lista de prendas dentro del JSON tenga al menos 2 prendas

    # json_data = {...}
    mis_datos = {"nombre": "Jack","apellido": "Sparrow","DNI": "123456789",
                "mi_ropa": [
                            {"prenda": "remeras","cantidad": 8,},
                            {"calzado": "zapatillas","cantidad": 6},
                            {"accesorios": "lentes","cantidad": 4}
                            ]}


    # Una vez que finalice el JSON realice un "dump" para almacenarlo en
    # un archivo que usted defina

    # Observe el archivo y verifique que se almacenó lo deseado
    with open('mi_json.json', 'w') as jsonfile:
        data = [mis_datos]
        print(data)  # Lo imprimí con este formato (como "LISTA") para ver 
                     # la diferencia cuando se INDENTA (como "JSON") 
    


def deserializar():
    print("Funcion que lee un archivo JSON")
    # JSON Deserialize
    # Basado en la función  anterior debe abrir y leer el contenido
    # del archivo y guardarlo en un objeto JSON utilizando el método
    # load()

    mis_datos = {"nombre": "Jack","apellido": "Sparrow","DNI": "123456789",
                "mi_ropa": [{"prenda": "remeras","cantidad": 8,},
                            {"calzado": "zapatillas","cantidad": 6},
                            {"accesorios": "lentes","cantidad": 4}
                            ]}



    with open('mi_json.json', 'w') as jsonfile:
        json.dump(mis_datos, jsonfile, indent=4)

    with open('mi_json.json', 'r') as jsonfile:
        json_misDatos = json.load(jsonfile)

    print(json.dumps(json_misDatos, indent=4))
    # Luego debe convertir ese JSON data en json_string utilizando
    # el método "dumps" y finalmente imprimir en pantalla el resultado
    # Recuerde utilizar indent=4 para poder observar mejor el resultado
    # en pantalla y comparelo contra el JSON que generó en la función anterior

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    serializar()
    deserializar()

    print("terminamos")