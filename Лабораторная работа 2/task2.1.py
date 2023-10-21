money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
months = 0
current_money = money_capital + salary  # Количество денег в данный момент

while True:
    current_money -= spend
    if current_money > 0:
        months += 1
    else:
        break
    spend += spend * increase
    current_money += salary
    
print("Количество месяцев, которое можно протянуть без долгов:", months)
