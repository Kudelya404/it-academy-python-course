"""1. Напишите программу, которая считает общую цену.
   Вводится M рублей и N копеек цена, а также количество S товара.
   Посчитайте общую цену в рублях и копейках за L товаров.
"""

mm: int = int(input())
nn: int = int(input())
ll: int = int(input())
dd = (((mm * 100) + nn) * ll)
print(f'Cтоимость {ll} товаров = {dd // 100} рублей, {dd % 100} копеек')
