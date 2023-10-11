numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
count_of_nums = len(numbers)
index = -1
for x in numbers:
    index += 1
    if x is None:
        break
if index != -1 and not(index == (count_of_nums - 1) and numbers[-1] is not None):
    numbers[index] = (sum(numbers[:index]) + sum(numbers[index+1:])) / count_of_nums
    print("Измененный список:", numbers)
else:
    print("Пропущенный элемент не найден")