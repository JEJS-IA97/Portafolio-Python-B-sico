from graphviz import Digraph

# Crear el objeto Digraph
dot = Digraph()

# Añadir los nodos y las flechas
dot.node("Ajuste de la perilla")
dot.edge("Ajuste de la perilla", "Agua fría")
dot.edge("Ajuste de la perilla", "Agua caliente")
dot.edge("Agua fría", "Mezcla")
dot.edge("Agua caliente", "Mezcla")
dot.edge("Mezcla", "Demora")
dot.edge("Demora", "Salida deseada")
dot.edge("Salida deseada", "Ajuste de la perilla", label="Realimentación negativa")
dot.edge("Salida deseada", "Ajuste de la perilla", label="Realimentación positiva")

# Dibujar el grafo
dot.render('diagrama_causal', view=True)
