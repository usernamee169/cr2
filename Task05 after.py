'''
Dynamic59: Добавление N чисел в конец двусвязного списка.

Даны ссылки A1, A2 и A3 на первый, последний и текущий элементы двусвязного списка
(если список пуст, A1 = A2 = A3 = null), число N (> 0) и набор из N чисел. Программа:
- Определяет класс IntList с полями first, last, current и методами InsertLast, Put.
- Добавляет N чисел в конец списка с помощью InsertLast.
- Выводит ссылки на первый, последний и текущий элементы, а также весь список.

Пользователь задает начальный список, N и набор чисел (могут быть строки, например, '00').
'''


from typing import Optional


class ClassNode:
    
    # FIXME: Классы нужно именовать с суффиксом Class: NodeClass
    def __init__(self, value: str) -> None:
        self.value = value
        self.prev: Optional["Node"] = None  # Ссылка на предыдущий узел
        self.next: Optional["Node"] = None  # Ссылка на следующий узел

    def put(self) -> str:
        return self.value


class IntListClass: # FIXME: Классы нужно именовать с суффиксом Class: IntListClass

    def __init__(self, first_node: Optional[Node], last_node: Optional[Node], current_node: Optional[Node]) -> None:
    # FIXME: Имена аргументов конструктора не соответствуют code style.
    # Исправление: Имена аргументов изменены на first_node, last_node и current_node.
        self.first = first_node
        self.last = last_node
        self.current = current_node

    def insert_last(self, str) -> None:
        new_node = Node(data)
        if not self.first:
            self.first = new_node
            self.last = new_node
            self.current = new_node
        else:
            self.last.next = new_node
            new_node.prev = self.last
            self.last = new_node
            self.current = new_node

    def put(self) -> None:
        '''Выводит ссылки на первый, последний и текущий элементы.'''
        first_val = self.first.put() if self.first else "null"
        last_val = self.last.put() if self.last else "null"
        current_val = self.current.put() if self.current else "null"
        print(f"Первый элемент (first): {first_val}")
        print(f"Последний элемент (last): {last_val}")
        print(f"Текущий элемент (current): {current_val}")

    def display_list(self) -> None:
        '''Выводит весь список в читаемом формате.'''
        if not self.first:
            print("Список пуст.")
            return

        current = self.first
        elements = []
        while current:
            elements.append(str(current.value))
            current = current.next
        print("Список: " + " <-> ".join(elements))


def get_user_input(prompt: str) -> str:
    '''Получает ввод от пользователя с заданным приглашением.'''
    return input(prompt).strip()


def create_initial_list() -> IntListClass:
    '''Создает начальный двусвязный список на основе ввода пользователя.'''
    nodes = []
    while True:
        try:
            count = int(get_user_input("Введите количество элементов в начальном списке (0 для пустого): "))
            if count < 0:
                print("Ошибка: Количество не может быть отрицательным.")
                continue
            break
        except ValueError:  # Обрабатываем некорректный ввод
            print("Ошибка: Введите целое число.")

    if count == 0:
        return IntListClass(None, None, None)

    for i in range(count):
        value = get_user_input(f"Введите значение элемента {i + 1} (например, '00' или '123'): ")
        nodes.append(Node(value))

    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
        nodes[i + 1].prev = nodes[i]

    int_list = IntListClass(nodes[0], nodes[-1], nodes[0])
    print("\nВаш начальный список:")
    int_list.display_list()

    while True:
        try:
            current_index = int(get_user_input("Выберите номер текущего элемента (1-{}): ".format(count))) - 1
            if 0 <= current_index < count:
                int_list.current = nodes[current_index]
                break
            print("Ошибка: Номер должен быть от 1 до", count)
        except ValueError:
            print("Ошибка: Введите целое число.")

    return int_list


def add_numbers_to_list(int_list: IntListClass) -> None:
    '''Добавляет N чисел в конец списка.'''
    while True:
        try:
            n = int(get_user_input("Введите количество чисел для добавления (N > 0): "))
            if n <= 0:
                print("Ошибка: N должно быть положительным числом.")
                continue
            break
        except ValueError:  
            print("Ошибка: Введите целое число.")

    for i in range(n):
        value = get_user_input(f"Введите число {i + 1} для добавления (например, '00' или '123'): ")
        int_list.insert_last(value)


def main() -> None:
    print("Добро пожаловать в программу добавления чисел в двусвязный список!")

    int_list = create_initial_list()

    add_numbers_to_list(int_list)

    print("\nРезультат после добавления чисел:")
    int_list.put()
    int_list.display_list()


if __name__ == "__main__":
    main()
