'''
Дано число N (> 0) и набор из N чисел. Создать стек, содержащий исходные числа
(последнее число будет вершиной стека), и вывести ссылку на его вершину.
'''

#FIXME: Некорректные отступы
class Node:
  def __init__(self, data=None, next=None):
    self.data = data
    self.next = next

class Stack:
  def __init__(self):
    self.head = None
  def push(self, data):
    newnode = Node(data, self.head) # FIXME: Имя переменной newnode не соответствует код стайлу.
    self.head = newnode 
  def __str__(self):
    elements = []
    current = self.head
    while current:
      elements.append(str(current.data))
      current = current.next
    return " -> ".join(elements)
  def pick(self): # FIXME: Название метода pick не отражает его функциональность.
    return self.head

N = int(input("Введите число N > 0: ")) # FIXME: Название переменной N не соответствует код стайлу.
numbers = []
for _ in range(N):
  number = int(input("Введите число: "))
  numbers.append(number)

stack = Stack()
for number in numbers:
  stack.push(number)

print("Ссылка на вершину стека:", stack.pick())
print("Содержимое стека:", stack)
