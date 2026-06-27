original_dict = {
    "A" : 1,
    "B" : 2
}

print(original_dict)

for key in list(original_dict.keys()):
    value = original_dict.pop(key)
    original_dict[value] = key

print(original_dict)