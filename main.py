def employeeProductivity():
# input statements
  employeeName = input("Enter Employee Name: ")
  numShifts = int(input("Enter number of shifts: "))
  numTransactions = int(input("Enter number of transactions: "))
  transDollarValue = float(input("Enter transactions dollar value: "))
  
#Productivity score calculation
  productivityScore = (transDollarValue / numTransactions) / numShifts 
  
# if statements
  if productivityScore <= 30:
    bonus = 50.00
  else:
    if productivityScore >= 31 and productivityScore <= 69:
      bonus = 75.00
    else: 
      if productivityScore >= 70 and productivityScore <= 199:
        bonus = 100.00
      else: 
        if productivityScore >= 200:
          bonus = 200.00
  
# output statements
  print("Employee Name: "+str(employeeName))
  print("Employee Bonus: $"+str(bonus))
  return "Employee Name: "+str(employeeName), \
  "Employee Bonus: $"+str(bonus)

if __name__ == "__main__":
  employeeProductivity()