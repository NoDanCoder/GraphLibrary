from abc import ABC, abstractmethod


# Edge abstract class
class Edge(ABC):

    @abstractmethod
    def get_relation_class(self):
        pass
