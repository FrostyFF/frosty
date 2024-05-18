def find_change(coins, amount):
    coins.sort(reverse=True)
    change=[]
    for coin in coins:
        while amount >= coin:
            change.append(coin)
            amount -= coin
        return change

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
print("Список продкутов: ")
for product in products:
    print(product)

product = input("\nВыберите товар: ").lower()
if product in products:
    price = products[product]
    payment = int(input("Укажите сумму: "))
    
    if payment >= price:
        change_due = payment - price
        coins = [1,5, 7, 10, 15]
        change_coins = find_change(coins, change_due)
        
        print(f"Сдача: {change_due}p")
        print("Количество монет для сдачи:")
        for coin in change_coins:
            print(coin, end="р ")
        if payment == price:
            print("Нет сдачи")
    else:
        print("Ты бомж!")
else:
    print("Нет в наличии")
