#'for' loop - dict
ages = {'kevin': 59, 'bob': 40, 'kayla': 21}
for key in ages:
    print(key)

for name, age in ages.items():
    print(f"Person Named: {name}")
    print(f"Age of: {age}")