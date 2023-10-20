#1 Проверка скобок
def check_brackets_balance(expression):
    opening_brackets = '([{'
    closing_brackets = ')]}'
    stack = []

    for char in expression:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack:
                return False  # Unbalanced expression
            top = stack.pop()
            if opening_brackets.index(top) != closing_brackets.index(char):
                return False  # Mismatched brackets

    return len(stack) == 0  # If the stack is empty, expression is balanced

expression = 'abs(math.sin(pow((5*a - b), 3)))'
is_balanced = check_brackets_balance(expression)
if is_balanced:
    print("Скобки сбалансированы")
else:
    print("Скобки не сбалансированы")

#2 Проверка на анаграмму
word1 = input().lower()
word2 = input().lower()

if sorted(word1) == sorted(word2):
    print("Правильно")
else:
    print("Не правильно")

#3 Среднее по величине число
z = int(input())
x = int(input())
c = int(input())

numbers = [z, x, c]
numbers.sort()
print(numbers[1])

#4 Смешивание цветов
color1 = input().lower()
color2 = input().lower()

if color1 == 'красный' and color2 == 'синий' or color1 == 'синий' and color2 == 'красный':
    print("фиолетовый")
elif color1 == 'красный' and color2 == 'желтый' or color1 == 'желтый' and color2 == 'красный':
    print("оранжевый")
elif color1 == 'синий' and color2 == 'желтый' or color1 == 'желтый' and color2 == 'синий':
    print("зеленый")
else:
    print("ошибка цвета")

#5 Сумма чисел оканчивающихся на 2, 5 или 8
n = int(input())
total_sum = 0

for num in range(11, n + 1):
    last_digit = num % 10
    if last_digit in {2, 5, 8}:
        total_sum += num

print(total_sum)

# Задание 6: Последовательность упорядочена по неубыванию
n = int(input())
digits = [int(digit) for digit in str(n)]

if digits == sorted(digits):
    print("Да")
else:
    print("Нет")

# Задание 7: Таблица размером n×5
n = int(input())
for i in range(1, n + 1):
    print(f"{i} {i} {i} {i} {i}")

#8 Работа с символами в строке
text = input()
print(text[2])
print(text[-2])
print(text[:5])
print(text[:-2])
print(text[::2])
print(text[1::2])
print(text[::-1])
print(text[::-1][::2])

#9 Формирование списка строк
result = [chr(97 + i) * (i + 1) for i in range(26)]
print(result)

#10 Подсчет пар элементов в списке
numbers = list(map(int, input().split()))
pairs = 0

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] == numbers[j]:
            pairs += 1

print(pairs)
