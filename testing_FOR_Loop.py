# Create a CLI Virtual mwnu that, based on timing of day, informs some dishes and possible restaurants to the 
# desired option

timing = input("Inform a time option: morning, noon or night: ")
breakfast_options = ["Eggs", "Pancakes", "Bacon", "Juice", "Coffee", "Cereal Flakes with Milk", "Piece of Cake", "Mapple Syrup"]
lunch_options = ["Peanut Butter and Jam Sandwich", "Salad", "Rice, French Fries and Meat", "Pasta", "Coffee with Croissaint"]
dinner_options = ["Pasta", "Chicken", "Chilli", "Salad", "Sandwich", "Mac'n Cheese"]

def show_breakfast_options():
    for option in breakfast_options:
        print(option)

def show_lunch_options():
    for option in lunch_options:
        print(option)

def show_dinner_options():
    for option in dinner_options:
        print(option)

if timing == "morning":
    show_breakfast_options()
elif timing == "noon":
    show_lunch_options()
elif timing == "night":
    show_dinner_options()
else:
    print("Invalid Option")

#meal