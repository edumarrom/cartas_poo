resultados = {'carlos': 6.0, 'emilio': 2.0, 'ines': 4.5}
valores = sorted(resultados.values()) # Sort the values
ordenado = {}
for i in valores:
    for k in resultados.keys():
        if resultados[k] == i:
            ordenado[k] = resultados[k]
            break
print(max(ordenado))

print(max(resultados))
