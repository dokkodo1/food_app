import json
import random

def main():
    selected_country = select_country()
    choose_dish(selected_country)

def select_country():
    yes = ["y", "yes", "yup", "yip"]
    no = ["n", "no", "nope"]

    with open("data/countries.json", "r") as f:
        data = json.load(f)

    while True:
        selected_country = random.choice(list(data["countries"].keys()))
        country_data = data["countries"][selected_country]

        print(f"\n{selected_country}\n{country_data['description']}")

        user_response = input("Would you like to choose a different country? (Yes/No)\n").strip().lower()
        
        if user_response in yes:
            continue
        elif user_response in no:
            print(f"\n{country_data['languages']}\n{country_data['greeting']}")
            return selected_country
        else:
            print("Invalid response.")
            continue

def choose_dish(country):
    with open("data/dishes.json", "r") as f:
        dish_data = json.loads(f)
    with open("data/countries.json", "r") as f:
        country_data = json.loads(f)
        
    dishes = country_data[country]["dishes"]

    for dish in dishes:
        print(f"{dish.name}\n{dish.description}") # replace
    while True:
        selected_dish = input("Which dish would you like to see?\n")
        if selected_dish not in dishes:
            print("Invalid dish")
            continue
        print(f"{selected_dish.recipe}\n{selected_dish.steps}") # replace
        break

if __name__ == "__main__":
    main()
