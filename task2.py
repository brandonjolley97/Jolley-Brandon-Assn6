
# Prompting user input for required variables.
employeeName = input("Please enter the employee's name: ")
hoursWorked = eval(input("Please enter the number of hours worked in a week: "))
payRate = eval(input("Please enter the hourly pay rate: "))
federalTax = eval(input("Please enter the federal withholding rate as a decimal (ex. 0.12): "))
stateTax = eval(input("Please enter the state withholding rate as a decimal (ex. 0.12): "))

# Computing desired output according to user info.
grossPay = hoursWorked * payRate
federalDeductions = federalTax * grossPay
stateDeductions = stateTax * grossPay
totalDeductions = federalDeductions + stateDeductions
netPay = grossPay - totalDeductions

# Formatting text to follow the example



# Displaying results to user.
print("Employee Name: " + employeeName + "\n" + "Hours Worked: " + str(hoursWorked) + "\n" + "Pay Rate: " + str(payRate) + "\n" + "Gross Pay: " + str(grossPay) + "\n" + "\n"
      + "Federal Withholding: " + str(federalDeductions) + "\n" + "State Withholding: " + str(stateDeductions) + "\n" "Total Withholding: " + str(totalDeductions) + "\n" + "Net Pay: " + str(netPay))





