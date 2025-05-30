'''
Дано число N (> 0) и набор из N чисел. Создать стек, содержащий исходные числа
(последнее число будет вершиной стека), и вывести ссылку на его вершину.
'''


class NodeClass:
    
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class StackClass:

    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = NodeClass(data, self.head)
        # FIXME: Имя переменной newnode не соответствует код стайлу.
        # Исправление: Переименовано в new_node.
        self.head = new_node

    def __str__(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next_node
        return " -> ".join(elements)

    def get_top(self):
        # FIXME: Название метода pick не отражает его функциональность.
        # Исправление: Метод переименован в get_top, чтобы отражать, что он возвращает верхний элемент стека.
        return self.head


#FIXME: Добавлена точка входа
if __name__ == '__main__':
    number_of_elements = int(input("Введите число N > 0: "))
    # FIXME: Название переменной N не соответствует код стайлу.
    # Исправление: Переименовано в number_of_elements.
    numbers = []
    for _ in range(number_of_elements):
        number = int(input("Введите число: "))
        numbers.append(number)

    stack = StackClass()
    for number in numbers:
        stack.push(number)

    print("Ссылка на вершину стека:", stack.get_top())
    print("Содержимое стека:", stack)
