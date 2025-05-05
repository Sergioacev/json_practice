import json
from collections import Counter

# Abrir el archivo JSON
with open('c:/Users/306/ganadores_goty.json', 'r', encoding='utf-8') as archivo:
    goty = json.load(archivo)
    
    # Inicializar listas
    generos = []
    desarrolladores = []
    detalle_juegos = []

    
    for juego in goty:
        genero = juego.get("género", "Desconocido")  
        desarrollador = juego.get("desarrollador", "Desconocido")  
        
        generos.append(genero)
        desarrolladores.append(desarrollador)
        detalle_juegos.append({
            "Año": juego.get("año", "Desconocido"),
            "Juego": juego.get("juego", "Desconocido"), 
            "Desarrollador": desarrollador,
            "Género": genero
        })

    conteo_generos = dict(Counter(generos))
    conteo_desarrolladores = dict(Counter(desarrolladores))

    
    resumen = {
        "Total Juegos": len(goty),
        "Juegos por Género": conteo_generos,
        "Juegos por Desarrollador": conteo_desarrolladores,
        "Detalle Juegos": detalle_juegos
    }

# Guardar archivo resumen
with open('resumen_goty.json', 'w', encoding='utf-8') as salida:
    json.dump(resumen, salida, ensure_ascii=False, indent=4)

# Mostrar resumen en consola
print("Resumen de Juegos del Año (GOTY):")
print(f"Total Juegos: {len(goty)}\n")

print("Juegos por Género:")
for genero, cantidad in conteo_generos.items():
    print(f"- {genero}: {cantidad}")

print("\nJuegos por Desarrollador:")
for dev, cantidad in conteo_desarrolladores.items():
    print(f"- {dev}: {cantidad}")

print("\nArchivo creado con éxito: resumen_goty.json")
