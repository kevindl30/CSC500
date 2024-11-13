# Create a variable to track points
points = 0

# Loop to get a valid integer input for the number of books purchased
while True:
    books_input = input("How many books were purchased this month? ")
    
    # Check if the input is a digit
    if books_input.isdigit():
        books = int(books_input)
        break  # Exit loop if input is valid
    else:
        print("Error - Please enter a valid input.")

# Calculate points based on the number of books purchased
if books == 0 or books == 1:
    points = 0
elif books == 2 or books == 3:
    points = 5
elif books == 4 or books == 5:
    points = 15
elif books == 6 or books == 7:
    points = 30
elif books >= 8:
    points = 60

# Display the number of points awarded
print(f"You have earned {points} points.")
