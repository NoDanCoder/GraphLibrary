from graph import Graph


# Clase ejemplo, para crear los nodos
class User:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


if __name__ == "__main__":
    graph = Graph()

    node1 = User("pepe")
    node2 = User("juan")
    node3 = User("paco")

    graph.connect_nodes(node1, node2)
    graph.connect_nodes(node1, node3)

    print(graph)

    print(graph.is_connected(node1, node3))
    print(graph.is_connected(node2, node3))

    any(print(x) for x in graph.get_connected_nodes(node1) if x is not node1)
