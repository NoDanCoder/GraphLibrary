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

    print(graph.is_connected(node1, node3) is True)
    print(graph.is_connected(node2, node3) is False)

    print(graph.get_connected_nodes(node1) == {node2, node3})
    print(graph.get_connected_nodes(node2) == {node1})
    print(graph.get_connected_nodes(node3) == {node1})
