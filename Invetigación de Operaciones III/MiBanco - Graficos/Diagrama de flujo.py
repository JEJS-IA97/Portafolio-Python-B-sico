import matplotlib.pyplot as plt
import networkx as nx

# Creamos un gráfico dirigido
G = nx.DiGraph()

# Agregamos los nodos
G.add_node("Inicio")
G.add_node("Llegada de clientes")
G.add_node("Clientes entran a la cola")
G.add_node("Cajeros disponibles?")
G.add_node("Cliente es atendido")
G.add_node("Cliente espera en la cola")
G.add_node("Cliente sale de la cola")
G.add_node("Fin")

# Agregamos las aristas
G.add_edges_from([
    ("Inicio", "Llegada de clientes"),
    ("Llegada de clientes", "Clientes entran a la cola"),
    ("Clientes entran a la cola", "Cajeros disponibles?"),
    ("Cajeros disponibles?", "Cliente es atendido"),
    ("Cliente es atendido", "Fin"),
    ("Cajeros disponibles?", "Cliente espera en la cola"),
    ("Cliente espera en la cola", "Cajeros disponibles?"),
    ("Cliente espera en la cola", "Cliente sale de la cola"),  # Modificación aquí
    ("Cliente sale de la cola", "Fin")
])

# Posiciones de los nodos
pos = {
    "Inicio": (0, 0),
    "Llegada de clientes": (1, 1),
    "Clientes entran a la cola": (2, 2),
    "Cajeros disponibles?": (3, 3),
    "Cliente es atendido": (4, 2),
    "Cliente espera en la cola": (4, 4),
    "Cliente sale de la cola": (5, 3),
    "Fin": (6, 1)
}

# Dibujamos el grafo con flechas de color naranja
nx.draw(G, pos, with_labels=True, node_size=2500, node_color="skyblue", font_size=10,
        arrowsize=25, width=2.5, edge_color='orange', arrowstyle="->")
plt.title("Diagrama de Flujo de Atención al Cliente", fontsize=14, pad=20)
plt.savefig("diagrama_flujo_cliente.png", transparent=True)  # Guardamos como PNG con fondo transparente
plt.show()
