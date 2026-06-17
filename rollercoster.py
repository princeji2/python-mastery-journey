print("Welcome to the Python Roller Coaster!")
height = int(input("What is your height in cm? \n"))
bill = 0

if height >= 120:
    print("You can ride the roller coaster!")
    age = int(input("What is your age? \n"))
    if age < 12:
      bill = 5 
      print("Please pay $5.")
    elif age <= 18:
      bill = 7
      print("Please pay $7.")
    elif age >= 45 and age <= 55:
        print("Everything is going to be ok. Have a free ride on us!")
    else:
      bill = 12
      print("Please pay $12.")
      if age >= 45 and age <= 55:
        print("Everything is going to be ok. Have a free ride on us!")
    wants_photo = input("Do you want a photo taken? Y or N. \n")
    if wants_photo == "Y":
        # Add the $3 cost to the total
      bill += 3
    print(f"Your final bill is ${bill}.")
else:
    print("Sorry, you have to grow taller before you can ride.")
    