# pcost.py
#
# Exercise 1.27
file = open('Data/portfolio.csv', 'rt')
headers = next(file).split(',')

total_cost = 0

for line in file:
    row = line.split(',')
    cost_of_shares = int(row[1])*float(row[2])
    total_cost += cost_of_shares

print(total_cost)

file.close()