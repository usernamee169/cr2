'''
Дан односвязный линейный список и указатель на голову списка P1. Необходимо вставить значение M перед каждым вторым
элементом списка, и вывести ссылку на последний элемент полученного списка P2.
При нечетном числе элементов исходного списка в конец списка вставлять не надо.
'''

class NodeClass:
# FIXME:Классы нужно именовать с суффиксом Class: NodeClass
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedListClass:
# FIXME: Классы нужно именовать с суффиксом Class: LinkedListClass
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = NodeClass(data)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_before_second(self, m):
        # FIXME: Имя метода не соответствует код стайлу.
        # Исправление: paste переименовано в insert_before_second
        """
        Вставляет значение m перед каждым вторым элементом списка.
        Проверяем, что есть следующий узел,
        Пропускаем первый элемент, вставляем перед вторым
        """ 
        if not self.head or not self.head.next:
            return

        current = self.head
        count = 1

        while current.next: 
            if count % 2 != 0:
                new_node = NodeClass(m)
                new_node.next = current.next
                current.next = new_node
                current = new_node.next
                count += 2
            else:
                current = current.next
                count += 1

    def get_last_element(self):
        '''Получаем указатель на последний элемент'''
        current = self.head
        if not current:
            return None
        while current.next:
            current = current.next
        return current

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()


if __name__ == "__main__":
    linked_list = LinkedListClass()

    num_elements = int(input("Введите количество элементов для добавления в список: "))
    for i in range(num_elements):
        data = input(f"Введите элемент {i+1}: ")
        linked_list.append(data)

    m = input("Введите значение m для вставки: ")
    linked_list.insert_before_second(m)  

    print("Измененный список:")
    linked_list.print_list()

    last_node = linked_list.get_last_element()

    if last_node:
        print(f"Последний элемент списка имеет значение: {last_node.data}, Ссылка : {last_node}")
    else:
        print("Список пуст")