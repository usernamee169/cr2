'''
Dynamic70. Даны ссылки A1 и A2 на первый и последний элементы двусвязного списка, 
реализованного в виде цепочки узлов, которая ограничена по краям константами null 
(если список пуст, то A1 = A2 = null). 
Преобразовать исходный список в циклический список (см. задание Dynamic55), 
снабженный барьерным элементом. Барьерный элемент должен иметь значение 0 
и быть связан своими свойствами Next и Prev с первым и последним элементом исходного списка 
(в случае пустого исходного списка свойства Next и Prev барьерного элемента должны 
указывать на сам барьерный элемент). 
Вывести ссылку на барьерный элемент полученного списка.
Не создавать новые объекты типа Node, за исключением барьерного элемента.
'''


class NodeClass:
    
# FIXME: Классы нужно именовать с суффиксом Class: NodeClass
    def __init__(self, key):
        self.key = key
        self.next = None
        self.prev = None


class DoublyLinkedListClass:
    
# FIXME: Классы нужно именовать с суффиксом Class: ListClass.
    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None

    def append(self, key):
        new_node = NodeClass(key)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node  # FIXME: Ошибка в логике: Должно быть self.tail.next = new_node
            new_node.prev = self.tail  # FIXME: Ошибка в логике: Должно быть new_node.prev = self.tail
            self.tail = new_node       # FIXME: Ошибка в логике: Неправильное обновление head
                                       # FIXME: Не нужно ничего возвращать

    def cycle(self, A1, A2):
        """Преобразует список в циклический с барьерным элементом."""
        barrier = NodeClass(0)
        if A1 is None and A2 is None:
            barrier.next = barrier
            barrier.prev = barrier
            return barrier

        barrier.next = A1
        barrier.prev = A2
        A1.prev = barrier
        A2.next = barrier
        return barrier

    def print_list(self):
        """Выводит элементы списка в консоль."""
        current = self.head
        output = []
        while current:
            output.append(str(current.key))
            current = current.next
        print(', '.join(output))


if __name__ == '__main__':
    list_ = DoublyLinkedListClass()
    list_.append(1)
    list_.append(2)
    list_.append(3)
    list_.append(4)
    list_.append(5)
    list_.append(6)

    A1 = list_.head
    A2 = list_.tail

    barrier = list_.cycle(A1, A2)

    print(barrier.key)
