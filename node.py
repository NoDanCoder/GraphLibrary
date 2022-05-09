from Relation import Relation


class Node:

    _printable_attr = set()  # type: Set[str]

    def __init__(self):
        self._relation = Relation()

    def connect_right(self, other, edge):
        self._relation.link_nodes(other, edge)

    def connect(self, other, edge):
        self.connect_right(other, edge)
        other.connect_right(self, edge)

    def is_connected(self, node):
        return self._relation.is_node_linked(node)

    def is_connected_by(self, node, clazz):
        return self._relation.is_node_linked_by(node, clazz)

    def connections(self):
        return self._relation.connected_nodes()

    def connections_by(self, clazz):
        return self._relation.connected_nodes_by(clazz)

    def __str__(self):
        clazz = f"{type(self).__name__}"
        properties = [f"{k.strip('_')}: {v}" for k, v in vars(self).items() if k in self._printable_attr]
        properties = ", ".join(properties)
        return f"({clazz} -> {properties})"