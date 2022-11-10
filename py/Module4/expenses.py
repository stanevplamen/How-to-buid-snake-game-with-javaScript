expenses = [10.50, 8, 5, 15, 20, 5, 3]
total = sum(expenses)

print("You spent $", total, " on lunch this week.", sep='')

s2 = 0
for expence in expenses:
    s2 = s2 + expence

print('my sum ' + str(s2))