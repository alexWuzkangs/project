name = input("Enter your name: ")
age = input("Enter your age: ")
age = int(age)
activity = [
    ("Music Jam Session", "2 hours", "easy", 5),
    ("Science Experiments Lab", "3 hours", "moderate", 10),
    ("Sport Leadership Training", "4 hours", "challenging", 12)]
print("\nChoose an activity:")
for i, act in enumerate(activity, 1):
    print(f"{i}. {act[0]} ({act[1]}, {act[2]}, ${act[3]} fee)")
activity_choice = int(input("Enter the number of your activity: "))
selected_activity = activity[activity_choice - 1]
print(f"You have chosen: {selected_activity[0]}")
print("\nMeal options:")
print("1. Standard")
print("2. Vegetarian")
print("3. Dairy-free")
print("4. No meal")
meal_choice = int(input("Enter the number of your meal: "))
meal_options = ["Standard", "Vegetarian", "Dairy-free", "No meal"]
selected_meal = meal_options[meal_choice - 1]
print(f"{name}, aged {age}, has chosen activity: '{selected_activity[0]}' and meal option: '{selected_meal}'.")