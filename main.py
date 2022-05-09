from Node import Node
from Edge import Edge


class User(Node):

    _printable_attr = {"_name"}

    def __init__(self, name):
        super().__init__()
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


class Friend(Edge):
    pass


class Enemy(Edge):
    pass


if __name__ == "__main__":
    user1 = User("Paco")
    user2 = User("Juan")

    print(user1)
    print(user2)

    friend = Friend()

    user1.connect_right(user2, friend)

    print(user1.is_connected(user2) is True)
    print(user2.is_connected(user1) is False)

    user3 = User("Paco")
    user4 = User("Iniesta")

    enemy = Enemy()

    user3.connect(user4, friend)
    user3.connect(user3, friend)
    user3.connect_right(user2, enemy)

    print(user3.is_connected(user4) is True)
    print(user4.is_connected(user3) is True)
    print(user3.is_connected(user2) is True)
    print(user2.is_connected(user3) is False)
    print(user4.is_connected(user2) is False)

    print(user1.is_connected_by(user2, Enemy) is False)
    print(user1.is_connected_by(user2, Friend) is True)

    any(print(f"{k}: {v}") for k, v in user3.connections())
    print()

    any(print(f"{x}") for x in user3.connections_by(Friend))
