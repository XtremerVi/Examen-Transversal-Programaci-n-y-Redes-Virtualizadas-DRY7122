import requests

url = "http://www.mapquestapi.com/directions/v2/route"

token = "4eaAz8Pb8zMberrCPCfdrMxpz3TvNhT1"

def obtener_distancia_duracion(origen,destino):
	params = {
		"key":token,
        "from":origen,
        "to":destino,
        "unit": "k",     
	}

	response = requests.get(url, params=params)
	data =response.json()

	distancia = data["route"]["distance"]
	duracion =data["route"]["formttadtime"]
	instrucciones = data ["route"]["legs"][0]["maneuvers"]

	return distancia, duracion, instrucciones

def imprimir_narrativa(distancia, duracion, instrucciones):
    combustible_requerido = combustible_requerido(distancia)
	
    print(f"Distancia del vieje): {distancia:.3f} km")
    print(f"Duracion estiamda: {duracion}")
    print(f"Combustible requerido: {combustible_requerido:.3f} lts")
    print("--------------------------------------------------------------")
    print("\nNarrativa del viaje")

    for i, instruccion in enumerate(instrucciones, 1):
        distancia = instruccion["distance"]
        calle = instruccion["narrative"]
        print(f"{i}. Avanza {distancia:.3d} metros por {calle}")

    def combustible_requerido(distancia):
         litros_por_kilometro = 0.07
         combustible_requerido = distancia
         return round(combustible_requerido, 3)

print("\n------------------------------------------")
origen = input("Ciudad de origen: ")
destino = input ("Ciudad de dedstino: ")
print("--------------------------------------------")

distancia, duracion, instrucciones = obtener_distancia_duracion(origen,destino)
imprimir_narrativa(distancia, duracion, instrucciones)

print("\n--------------------------------------------------------")
salida = input("\nPresione P para salir: ")

      
                