immutable_var = (1, "Arr", True)
print(f"Immutable tuple: {immutable_var}")
mutable_var = [1, "Arr", True]
print(f"Mutable list: {mutable_var}")
mutable_var[0] = 2
print(f"New mutable list: {mutable_var}")