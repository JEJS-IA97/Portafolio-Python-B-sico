def politica_reemplazo_pedido_fijo(demanda, inventario_inicial, punto_reorden, cantidad_pedido):
    inventario = inventario_inicial
    periodo = 1
    total_costo = 0

    while periodo <= len(demanda):
        if inventario < punto_reorden:
           
            pedido = cantidad_pedido
            total_costo += pedido * costo_pedido
            inventario += pedido

        demanda_periodo = demanda[periodo - 1]
        inventario -= demanda_periodo

        if inventario < 0:
          
            total_costo += abs(inventario) * costo_agotamiento
            inventario = 0

        periodo += 1

    return total_costo


demanda = [10, 15, 12, 18, 20]  # Demanda en cada período
inventario_inicial = 5          # Inventario inicial
punto_reorden = 10              # Punto de reorden
cantidad_pedido = 30            # Tamaño fijo del pedido
costo_pedido = 100              # Costo por realizar un pedido
costo_agotamiento = 10          # Costo por unidad agotada

costo_total = politica_reemplazo_pedido_fijo(demanda, inventario_inicial, punto_reorden, cantidad_pedido)
print(f"Costo total: {costo_total}")
