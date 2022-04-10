from typing import Set

from node import Node
from relation import Relation


class Graph:

    def __init__(self) -> None:
        self._relation = Relation()

    def connect_nodes(self, node_a: Node, node_b: Node) -> None:
        self._relation.bind_nodes(node_a, node_b)

    def is_connected(self, node_a: Node, node_b: Node) -> bool:
        return self._relation.is_related(node_a, node_b)

    def get_connected_nodes(self, node: Node) -> Set[Node]:
        return self._relation.get_siblings(node)

    def __str__(self) -> str:
        return str(self._relation)
