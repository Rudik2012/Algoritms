# Задание 1
# Найти сумму и произведение цифр трехзначного числа,
# которое вводит пользователь.

# сумма
# #num = int(input('Введите трехзначное число:'))
# sum = 0
# while num != 0:
#     sum += num % 10
#     num = num // 10

# #print(sum)

# произведение
# num = int(input('Введите трехзначное число:'))
# mult = 1
# while num != 0:
#     n = num % 10
#     num = num // 10
#     mult *= n
# print(mult)

# Задание 5
# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят,
# и сколько между ними находится букв.

# def letter_place(a: str, b: str):
#     a1 = ord(a) - ord('а') + 1
#     b2 = ord(b) - ord('а') + 1
#     print('Первая буква :', a1, 'Втоорая буква :', b2)
#     if a1 > b2:
#         print('Между ними ',a1 - b2 -1, 'букв')
#     if a1 < b2:
#         print('Между ними ',b2 - a1 - 1, 'букв')
#     else:
#         print('Вы ввели одинаковые буквы')
#
# print(letter_place('а', 'т'))

# Задание 8
# Определить, является ли год, который ввел пользователем,
# високосным или не високосным.

# def year_v(year):
#     if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#         print(year, 'Высокосный')
#     else:
#         print(year, 'Невысокосный')
#
# print(year_v(1980))


# class Solution:
#     def removeDuplicates(self, nums: list[int]) -> int:
#         last = nums[0]
#         j = 1
#
#         for i in range(1, len(nums)):
#             if nums[i] != last:
#                 nums[j] = nums[i]
#                 last = nums[i]
#                 j += 1
#         return j


class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        n = 0
        for i in range(len(nums)):
            idx = i - n
            if nums[idx] == 0:
                nums.pop(idx)
                nums.append(0)
                n += 1



