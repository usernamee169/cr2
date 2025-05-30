"""
Дан односвязный линейный список и указатель на голову списка P1. Необходимо
найти второй элемент, кратный 6, и вывести указатель на этот элемент списка Px. Если такого
элемента в списке нет, то результат должен быть равен nil.
"""

class NodeClass:  # FIXME: Классы нужно именовать с суффиксом Class: NodeClass
    def __init__(self, data, next=None):
        self.data = data
        self.next_node = next

    def __str__(self):
        return str(self.data)


def find_second_multiple_of_six(head_node):
    # FIXME: Имя аргумента P1 не соответствует код стайлу.
    # Исправление: Переименовано имя аргумента P1 в head_node.
    count = 0
    current = head_node
    while current is not None:
        if current.data % 6 == 0:
            count += 1
            if count == 2:
                return current
        current = current.next_node
    return None


if __name__ == "__main__":
    node5 = NodeClass(18)
    node4 = NodeClass(5, node5)
    node3 = NodeClass(12, node4)
    node2 = NodeClass(7, node3)
    node1 = NodeClass(6, node2) 

    result = find_second_multiple_of_six(node1)
    if result is None:
        print("В списке нет второго элемента, кратного 6.")
    else:
        print("Узел, являющийся вторым элементом, кратным 6, имеет значение:", result.data)