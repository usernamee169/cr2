'''
Dynamic26. Даны ссылки A1 и A2 на начало и конец очереди (если очередь является пустой,
то A1 = A2 = null). Также дано число N (> 0) и набор из N чисел. Описать класс IntQueue,
содержащий следующие члены:
 • закрытые поля head и tail типа Node (начало и конец очереди);
 • конструктор с параметрами aHead, aTail — началом и концом существующей очереди;
 • процедура Enqueue(D), которая добавляет в конец очереди новый элемент со значением D (D
 — входной параметр целого типа);
 • процедура Put (без параметров), которая выводит ссылки на поля head и tail, используя метод
Put класса PT.
С помощью метода Enqueue добавить в исходную очередь данный набор чисел и вывести
новые ссылки на ее начало и конец, используя для этого метод Put класса IntQueue.
'''


#FIXME: Исправлены некорректные отступы
class Node:
 
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class IntQueueClass: # FIXME: Классы нужно именовать с суффиксом Class: IntQueueClass

    def __init__(self, head_node=None, tail_node=None):
        # FIXME: Имена аргументов конструктора не соответствуют code style.
        # Исправление: Имена аргументов изменены на head_node и tail_node.
        self.head = head_node
        self.tail = tail_node

    def enqueue(self, data):
        # FIXME: Имя метода не соответствует code style.
        # Исправление: Имя метода изменено на enqueue.
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def put(self):
        # FIXME: Имя метода не соответствует code style.
        # Исправление: Имя метода изменено на put.
        print(f"Ссылка на начало очереди {self.head}")
        print(f"Ссылка на конец очереди {self.tail}")


if __name__ == "__main__":
    queue = IntQueueClass()
    # FIXME: Не используется try-except для обработки некорректного ввода.
    # Добавлена обработка исключения ValueError.
    try:
        n_elements = int(input("Введите число N (>0): "))
        if n_elements <= 0:
            print("N должно быть больше 0!!!")
        else:
            for _ in range(n_elements):
                try:
                    data = int(input("Введите число: "))
                    queue.enqueue(data)
                except ValueError:
                    print("Некорректный ввод. Введите целое число.")
    except ValueError:
        print("Некорректный ввод. Введите целое число.")

    queue.put()
