monthly_expenses = [2200, 2350, 2600, 2130, 2190]

print(monthly_expenses[1] - monthly_expenses[0])
print(sum(monthly_expenses[:3]))
print(2000 in monthly_expenses)
monthly_expenses.append(1980)
monthly_expenses[3] -= 200
print(monthly_expenses)


heros = ['spider man','thor','hulk','iron man','captain america']

print(len(heros))
heros.append("black panther")
heros.insert(heros.index("hulk")+1, heros.pop())
heros[1:3] = ["doctor strange"]
heros.sort()
print(heros)


num = input("give max : ")
odd = [i for i in range(int(num)) if i%2 != 0]
print(odd)