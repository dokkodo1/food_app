import json
import random


def main():
    print(select_country())



def select_country():
    with open("data/countries.json", "r") as f:
        data = json.load(f)
    for key, value in data["countries"].items():
        return key

    
    
main()