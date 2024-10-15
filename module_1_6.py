my_dict = {"Karl": 1980, "Olga":1985, "Alex":1982}
# Словарь
print(my_dict)
print("Существующий ключ:", my_dict["Olga"])
print("Несуществующий ключ:", my_dict.get("Masha", "Ключ не найден!"))
my_dict.update({"Sasha": 1986, "Roma": 1988})
n = my_dict.pop("Alex")
print(n)
print(my_dict)
print("-----------------------------------------")

# Множества
my_set = {1, 2, 1, 2, 3, 1.5, 2.2, 1.5, "Pavel",  "Pavel"}
print(my_set)
my_set.add(8)
my_set.add("Urban")
my_set.discard(2.2)
print(my_set)
