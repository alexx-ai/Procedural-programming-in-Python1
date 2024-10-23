numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
total = 0
count = len(numbers)
for i, num in enumerate(numbers):
  if num is not None:
    total += num
  else:
    index_of_none = i

average = total / count  # Исправленная строка
numbers[index_of_none] = average

print("Измененный список:", numbers)