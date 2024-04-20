def buscar_datos(*args, **kwargs):
    for key, value in kwargs.items():
        if all(arg in value.values() for arg in args):
            return key
    print("No se encontró el resultado.")
    return None

database = {
    "Persona1": {
        "primer_nombre": "Pablo",
        "segundo_nombre": "Diego",
        "primer_apellido": "Ruiz",
        "segundo_apellido": "Picasso"
    } ,
        "Persona2": {
            "primer_nombre": "Melina",
            "segundo_nombre": "Abril",
            "primer_apellido": "Gomez",
            "segundo_apellido": "Torres"
        },
        "Persona3": {
            "primer_nombre": "Candela",
            "segundo_nombre": "Agustina",
            "primer_apellido": "Gonzales",
            "segundo_apellido": "Privitera"
        },
        "Persona4": {
            "primer_nombre": "Rocio",
            "segundo_nombre": "Pilar",
            "primer_apellido": "Portal",
            "segundo_apellido": "Romano"
        } ,
        "Persona5": {
            "primer_nombre": "Maria",
            "primer_apellido": "Flores",
            "segundo_apellido": "Moyano"
        } ,
        "Persona6": {
            "primer_nombre": "Tomas",
            "primer_apellido": "Zapata",
        }
}

# Devuelve "Resultado encontrado"

resultado = buscar_datos("Pablo", "Diego", "Ruiz", "Picasso", **database)
if resultado is not None:
    print("Resultado encontrado:", resultado)


resultado = buscar_datos("Melina", "Abril", "Gomez", "Torres", **database)
if resultado is not None:
    print("Resultado encontrado:", resultado)


resultado = buscar_datos("Gomez", "Torres", **database)                                 
if resultado is not None:
    print("Resultado encontrado:", resultado)
                      
                                                                                                # --> Ejemplos funcionales de valores no completos
resultado = buscar_datos("Abril", **database)                             
if resultado is not None:
    print("Resultado encontrado:", resultado)


resultado = buscar_datos("Candela", "Agustina", "Gonzales", "Privitera", **database)
if resultado is not None:
    print("Resultado encontrado:", resultado)


resultado = buscar_datos("Rocio", "Pilar", "Portal", "Romano", **database)
if resultado is not None:
    print("Resultado encontrado:", resultado)


resultado = buscar_datos("Maria", "Flores", "Moyano", **database)
if resultado is not None:
    print("Resultado encontrado:", resultado)


resultado = buscar_datos("Tomas", "Zapata", **database)
if resultado is not None:
    print("Resultado encontrado:", resultado)


#Devuelve "No se encontró el resultado"


resultado = buscar_datos("Pablo", "Diego", "Portal", "Picasso", **database)
if resultado is not None:
    print("Resultado encontrado:", resultado)

resultado = buscar_datos("Melina", "Candela", "Portal", "Flores", **database)
if resultado is not None:
    print("Resultado encontrado:", resultado)

resultado = buscar_datos("Marina", "Rivadeneira", **database)
if resultado is not None:
    print("Resultado encontrado:", resultado)

resultado = buscar_datos("Candela", "Agustina", "Gonzales", "Pribitera", **database)          # --> Ejemplo de valor mal ingresado              
if resultado is not None:
    print("Resultado encontrado:", resultado)



