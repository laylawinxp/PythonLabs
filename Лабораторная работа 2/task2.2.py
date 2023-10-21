salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
sum_salary = 0
sum_spend = 0

for _ in range(months):
    sum_spend += spend
    spend += spend * increase
    sum_salary += salary
if sum_spend > sum_salary:
    money_capital = sum_spend - sum_salary
else:
    money_capital = 0
    
print(f"Подушка безопасности, чтобы протянуть {months :} месяцев без долгов:{money_capital : .2f}")
