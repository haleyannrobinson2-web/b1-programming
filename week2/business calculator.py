
print("Welcome to Business Calculator")

#revenue - expenses = profit
revenue = int(input("enter revenue"))
expenses = int(input("enter expenses"))
profit = revenue - expenses
print("Your profit is " + str(profit))
#calculate profit margin percentage

margin = profit / revenue *100
print("Your profit margin is ", margin,"%")

