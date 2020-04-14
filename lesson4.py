split = [3, 5, 7, 9, 10.5]
print(split)
split.append("Pyton")
print(split)
print(len(split))
print(split[0])
print(split[-1])
print(split[1:4])
split.remove("Pyton")
print(split)
print("///////////////////////////////////")
product = {'name': 'Iphone XS', 'stock': 5, 'price': 7800}
print(product)
product['stock'] = 10

house = {"city": 'Moscov', "temperature": '20'}
print(house)
print(house.get("city"))
print(house.get("temperature"))
house["temperature"] = int(house["temperature"]) - 5
print(house)
print(house.get("country"))
print(house.get("country", "Russian"))
print(house)
house["date"] = '27.05.2019'
print(house)
print(len(house))
