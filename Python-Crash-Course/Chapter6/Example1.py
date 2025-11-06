my_list = [3,3,9,4,2]
unique_items = set(my_list)
print(unique_items)
for item in unique_items:
    print(f"{item}: {my_list.count(item)}")