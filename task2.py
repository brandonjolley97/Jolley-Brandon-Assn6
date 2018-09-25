
# Prompting user input for required variables.
employeeName = input("Please enter the employee's name: ")
hoursWorked = eval(input("Please enter the number of hours worked in a week: "))
payRate = eval(input("Please enter the hourly pay rate: "))
federalTax = eval(input("Please enter the federal withholding rate as a decimal (ex. 0.11): "))
stateTax = eval(input("Please enter the state withholding rate as a decimal (ex. 0.11): "))

# Computing desired output according to user info.
grossPay = hoursWorked * payRate
federalDeductions = federalTax * grossPay
stateDeductions = stateTax * grossPay
totalDeductions = federalDeductions + stateDeductions
netPay = grossPay - totalDeductions


# Displaying results to user.


employeeInfo = employeeName.upper() + " PAY INFORMATION" + "\n\n"
grossPayInfo = "Hours Worked: " + str(hoursWorked) + "\n" + "Pay Rate: " + str(payRate) + "\n" + "Gross Pay: " + str(grossPay) + "\n\n"
deductionsInfo = "Federal Withholding: " + str(federalDeductions) + "\n" + "State Withholding: " + str(stateDeductions) + "\n" "Total Withholding: " + str(totalDeductions) + "\n"
netInfo = "Net Pay: " + str(netPay)

# Formatting text to follow the example
print("\n\n" + format(employeeInfo, "^40"))
print(format("Pay", "^45"))

print(format("Deductions", "^45"))








