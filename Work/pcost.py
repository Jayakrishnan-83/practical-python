# pcost.py
#
# Exercise 1.27

def portfolio_cost(filename):

    file = open(filename, 'rt')
    headers = next(file).split(',')

    total_cost = 0


    for line in file:
        row = line.split(',')
        cost_of_shares = int(row[1])*float(row[2])
        total_cost += cost_of_shares

    file.close()

    return total_cost

cost = portfolio_cost('Data/portfolio.csv')
print(f"total cost:{cost}")