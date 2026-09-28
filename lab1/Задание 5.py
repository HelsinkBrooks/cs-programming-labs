distance = int(input()) / 100
rashod = float(input())
stoimost = float(input())

fuel_itog = distance * rashod
money = fuel_itog * stoimost
print(f'Топливо: {fuel_itog:2f}')
print(f'Стоимость: {money:2f}')