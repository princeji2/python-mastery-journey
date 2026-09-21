import random 

random_number = random.randint(1, 100)
print(random_number)

random_float = random.random() * 5 
# random.random() generates a random float between 0.0 and 1.0, multiplying it by 5 scales it to a range of 0.0 to 5.0
print(random_float)

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}.")

