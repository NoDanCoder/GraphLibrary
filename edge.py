class Edge:

    def __init__(self):
        self._relation_dict = {}  # cada instacia tiene su propio diccionario

    def bind_nodes(self, node_a, node_b):
        self._relation_dict.setdefault(node_a, set()).add(node_b)
        self._relation_dict.setdefault(node_b, set()).add(node_a)

    def is_related(self, node_a, node_b):
        return node_b in self._relation_dict[node_a]

    def get_siblings(self, node):
        return self._relation_dict[node]

    def __str__(self):
        return "".join(f"{k}: " + ", ".join(str(x) for x in v) + "\n"
                       for k, v in self._relation_dict.items()) # Lista por comprension
