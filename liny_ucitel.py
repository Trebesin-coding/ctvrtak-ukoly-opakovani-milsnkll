import random
import json

smth = random.randint(1, 5)
print(smth)

jmeno = input("napis jmeno: ")

imena = ["biba", "boba", "belka", "strelka"]

if jmeno not in imena:
    odpoved = input(f"{jmeno} neni, pridat? (a/n): ") 
    if odpoved == "a":
        imena.append(jmeno)
        print(f"Student {jmeno} byl zapsan")
    else:
        print("konec")
        exit()

print("ty jsi", jmeno)



path = "data/data.json"

# data = {}
with open(path, mode="r") as file:
    load_data = json.load(file)

    if len(load_data) > 0:
        data = load_data
    else:
        data = {jmeno: smth}   


data[jmeno] = smth

with open(path, "w") as file:
    json.dump(data, file)

