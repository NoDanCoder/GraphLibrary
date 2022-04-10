from relation import Relation


class Graph:

    def __init__(self):
        self._relation = Relation()

    def connect_nodes(self, node_a, node_b):
        self._relation.bind_nodes(node_a, node_b)

    def is_connected(self, node_a, node_b):
        return self._relation.is_related(node_a, node_b)

    def __str__(self):
        return str(self._relation)

    def get_connected_nodes(self, node):
        return self._relation.get_siblings(node)
