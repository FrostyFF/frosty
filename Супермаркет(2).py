def find_change(coins, amount, available_coins):
    coins.sort(reverse=True)
    change = []
    for coin in coins:
        while amount >= coin and available_coins[coin] > 0:
            change.append(coin)
            amount -= coin
            available_coins[coin] -= 1
    return change

available_coins = {1: 0, 5: 4, 10: 0, 15: 0, 20: 0}
coins = [20, 15, 10, 5, 1]

products = {
    "молоко": 20,
    "хлеб": 30,
    "колбаса": 15,
    "пельмени": 50,
    "яйца С1": 90,
    "Йогурт": 80,
    "Орео": 45,
    "сахар 100гр": 10,
}

print("Список продуктов:")
for product in products:
    print(product)

product = input("\nВыберите товар: ").lower()
if product in products:
    price = products[product]
    payment = int(input("Укажите сумму: "))
    
    if payment >= price:
        change_due = payment - price
        change_coins = find_change(coins, change_due, available_coins)
        if len(change_coins) == len(coins):
            print("Не хватает монет для сдачи")
        else:
            print(f"Сдача: {change_due}p")
            print("Количество монет для сдачи:")
            for coin in change_coins:
                print(coin, end="р ")
                available_coins[coin] += 1
    else:
        print("Ты бомж!")
else:
    print("Нет в наличии")
