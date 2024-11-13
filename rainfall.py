# Initialize rainfall variable
rainfall = 0.0

# List of month names
months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]

# Enter number of years
years = int(input("Enter the number of years: "))

# Outer loop: Iterate over each year
for year in range(1, years +1):
    print(f"\nYear {year}")
    # Inner loop: Iterate over each month
    for month in months: # month will be the actual month name (e.g., "January")
        monthly_rainfall = float(input(f"Enter the rainfall (in inches) for {month}: "))
        rainfall += monthly_rainfall

# Calculate average rainfall
average_rainfall = rainfall / (len(months) * years)

# Output
print(f"\nNumber of months:", len(months) * years)
print(f"Total inches of rainfall: {rainfall:.2f}")
print(f"Average rainfall per month: {average_rainfall:.2f}")
