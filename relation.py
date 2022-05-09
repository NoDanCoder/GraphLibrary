class Relation:

    def __init__(self):
        self._node_edge_relation = {}
        self._clazz_node_relation = {}

    def link_nodes(self, node, edge):
        self._node_edge_relation[node] = edge
        self._clazz_node_relation.setdefault(type(edge), set()).add(node)

    def is_node_linked(self, node):
        return node in self._node_edge_relation.keys()

    def is_node_linked_by(self, node, clazz):
        edge = self._node_edge_relation[node]
        return isinstance(edge, clazz)

    def connected_nodes(self):
        return self._node_edge_relation.items()

    def connected_nodes_by(self, clazz):
        try:
            return self._clazz_node_relation[clazz]
        except KeyError:
            return set()