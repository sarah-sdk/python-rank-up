# EXERCICE 1 : liste de courses
shopping_list = ["bombe tue mouche", "bananes", "skyr"]
print(shopping_list)

add = input("Something to add? ")
shopping_list.append(add)
print(shopping_list)

shopping_list.pop(0)
print(shopping_list)

print(len(shopping_list))

for item in shopping_list:
  print(item)