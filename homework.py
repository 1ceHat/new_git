my_dict = {'Artem':2004, 'Dasha':2004}
print(f"Dict: {my_dict}")
print(f"Existing value: {my_dict['Artem']}")
my_dict.update({'Nikita':2003, 'Polina':2007})
print(f"Deleted value: {my_dict.pop('Dasha')}")
print(f"Modified dictionary: {my_dict}")

my_set = {1,2,1,'Artem', 'Dasha', 'Artem'}
print(f"\nSet: {my_set}")
my_set.add(3)
my_set.add(False)
my_set.discard(1)
print(f"Modified set: {my_set}")