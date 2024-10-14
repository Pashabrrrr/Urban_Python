immutable_var = 1, "name", 2.5
print(immutable_var)
print(type(immutable_var))
print("элементы кортежа нельзя изменить, т.к. кортеж - неизменяемая структура, ")
print("но он может содержать изменяемые элементы, например списки")

mutable_list = ["name", 2, 10.5]
print(mutable_list)
mutable_list[0] = "Pavel"
print(mutable_list)
