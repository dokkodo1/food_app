import sys
import json
import random


def main():
    print(select_country())
#   choose_dish(select_country)


def select_country():
    yes = ["y", "yes", "yup", "yip"]
    no = ["n", "no", "nope"]
    with open("data/countries.json", "r") as f:
        data = json.load(f)

    while True:
        selected_country = random.choice(data["countries"])
        print(f"{selected_country}\n{selected_country.description}")
        user_response = input("Would you like to choose a different country?\n\"Yes\", \"No\"\n")
        if user_response in yes:
            continue
        elif user_response in no:
            print(f"{selected_country.languages}\n{selected_country.greeting}")
            return selected_country
        else:
            print("Invalid response")
            continue


def choose_dish(country):
    with open("data/dishes.json", "r") as f:
        data = json.load(f)
    dishes = data[{country}]

    for dish in dishes:
        print(f"{dish.name}\n{dish.description}")
    while True:
        selected_dish = input("Which dish would you like to see?\n")
        if selected_dish not in dishes:
            print("Invalid dish")
            continue
        print(f"{selected_dish.recipe}\n{selected_dish.steps}")
        break

    
if __name__ == "__main__":
    main()