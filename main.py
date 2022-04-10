from graph import Graph
from node import Node


class User(Node):

    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
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

    print(" ".join(str(x) for x in graph.get_connected_nodes(node1)))
