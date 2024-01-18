# Display program greeting
print("\nWelcome to the Tip calculator.")

# Get user input on bill information
bill = float(input("What was the total bill? $"))
people = int(input("How many people to split the bill? "))
percentage = float(input("What percentage tip would you like to give? 10, 12, or 15? "))

# Calculate total bill with tip
bill = bill + bill * (percentage / 100)

# Caculate bill for each person
person_bill = bill / people

# Print bill for each person
print(f"Each person should pay: ${person_bill:.1f}\n")