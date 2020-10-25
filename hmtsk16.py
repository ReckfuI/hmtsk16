d = {'One': '1', 'Two': '2', 'Three': '3', 'Four': None, 'Five': '5', 'Six': None }
for key in list(d):
    if d[key] is None:
        del d[key]
print(d)