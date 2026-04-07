def worked_hours(hourly_rate, hours_worked):
    return hourly_rate * hours_worked

def calculate_salary(hourly_rate, hours_worked):
    return worked_hours(hourly_rate, hours_worked)

def Discounts(salary, INSS_tax_percentage, IRFF_tax_percentage, Union_fee_percentage):
    INSS_tax = salary * (INSS_tax_percentage / 100)
    IRFF_tax = salary * (IRFF_tax_percentage / 100)
    Union_fee = salary * (Union_fee_percentage / 100)
    total_deductions = INSS_tax + IRFF_tax + Union_fee
    net_salary = salary - total_deductions
    return net_salary

input_hourly_rate = float(input("Enter your hourly rate: "))
input_hours_worked = float(input("Enter hours worked: "))
gross_salary = calculate_salary(input_hourly_rate, input_hours_worked)
print(f"Gross Salary: ${gross_salary:.2f}")
INSS_tax_percentage = float(input("Enter INSS tax percentage: "))
IRFF_tax_percentage = float(input("Enter IRFF tax percentage: "))
Union_fee_percentage = float(input("Enter Union fee percentage: "))
net_salary = Discounts(gross_salary, INSS_tax_percentage, IRFF_tax_percentage, Union_fee_percentage)
print(f"Net Salary: ${net_salary:.2f}")