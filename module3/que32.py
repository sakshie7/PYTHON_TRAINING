# Write a Python script to sort (ascending and descending) a dictionary by value
value = {
     "marks a":67,
     "marks a":74,
     "marks a":88,
     "marks a":96,
     "marks a":50,
}
print(value)

stored_value = dict(sorted(value.items(), key=lambda item : item[1]))
print(stored_value)

stored_value_desc = dict(sorted(value.items(), key=lambda item : item[1],reverse=True))
print(stored_value_desc)