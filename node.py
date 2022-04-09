from abc import ABC, abstractmethod


# Node abstract class
class Node(ABC):

    @abstractmethod
    def get_node_class(self):
        pass
