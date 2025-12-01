# dictionaries = A collection of {key:value} pairs ordered and changeable. No duplicates

capitals = {"USA": "Detroit",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

print(capitals.get("USA"))

capitals.update({"Germany": "Berlin"})
capitals.update({"USA": "Washington D.C."})
capitals.pop("China")

for key in capitals.keys():
    print(key)

for value in capitals.values():
    print(value)
    
for key, value in capitals.items():
    print(f"{key}: {value}")