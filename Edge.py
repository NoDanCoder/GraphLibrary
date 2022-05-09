from typing import Set


class Edge:

    _printable_attr = set()  # type: Set[str]

    def __str__(self):
        clazz = f"{type(self).__name__}"
        properties = [f"{k.strip('_')}: {v}" for k, v in vars(self).items() if k in self._printable_attr]
        properties = ", ".join(properties)
        return f"[{clazz} -> {properties}]"