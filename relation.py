from typing import Set, Dict

from node import Node


class Relation:

    def __init__(self) -> None:
        self._edge_dict = {}  # type: Dict[Node, Set[Node]]

    def bind_nodes(self, node_a: Node, node_b: Node) -> None:
        self._edge_dict.setdefault(node_a, set()).add(node_b)
        self._edge_dict.setdefault(node_b, set()).add(node_a)

    def is_related(self, node_a: Node, node_b: Node) -> bool:
        return node_b in self._edge_dict[node_a]

    def get_siblings(self, node: Node) -> Set[Node]:
        return self._edge_dict[node]

    def __str__(self) -> str:
        return "".join(f"{k}: " + ", ".join(str(x) for x in v) + "\n"
                       for k, v in self._edge_dict.items())
