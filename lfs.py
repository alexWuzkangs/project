#This program asks the user to their name and age 
name = input("Enter your name: ")
age = input("Enter your age: ")
age = int(age)

activity = [
    ("Music Jam Session", "2 hours", "easy", 5),
    ("Science Experiments Lab", "3 hours", "moderate", 10),
    ("Sport Leadership Training", "4 hours", "challenging", 12)]
print("\nChoose an activity:")
#forloop is used to enter element into a list 
for i, act in enumerate(activity, 1):
    print(f"{i}. {act[0]} ({act[1]}, {act[2]}, ${act[3]} fee)")
activity_choice = int(input("Enter the number of your activity: "))
selected_activity = activity[activity_choice - 1]
#the lines bellow will print the meal options for us 
print(f"You have chosen: {selected_activity[0]}")
print("\nMeal options:")
print("1. Standard")
print("2. Vegetarian")
print("3. Dairy-free")
print("4. No meal")
meal_choice = int(input("Enter the number of your meal: "))
meal_options = ["Standard", "Vegetarian", "Dairy-free", "No meal"]
selected_meal = meal_options[meal_choice - 1]
#this line tells the user all of their entered infomation 
print(f"{name}, aged {age}, has chosen activity: '{selected_activity[0]}' and meal option: '{selected_meal}'.")
print ("hello")