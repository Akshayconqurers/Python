# Data from user

total_bill = float(input("Total amount of Bill : "))
tip_percentage = float(input("Enter the tip percentage you want to give: "))
people_Number = int(input("Number of people splitting the bill: "))


tip_amount = total_bill * (tip_percentage / 100)
total_amount = total_bill + tip_amount


amount_per_person = total_amount / people_Number

print(f"Tip Amount: {tip_amount:.2f}")
print(f"Total Amount (Bill + Tip): {total_amount:.2f}")
print(f"Each person should pay: {amount_per_person:.2f}")

# Using :.2f ensures the output is always formatted to 2 decimal places,
# making it readable and consistent for currency values (e.g., $12.34).
