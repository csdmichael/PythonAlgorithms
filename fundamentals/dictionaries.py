phonebook = {}
phonebook["John"] = 123456788
phonebook["Mike"] = 98765432
phonebook["Sarah"] = 53445445
print(phonebook)

phonebook2 = {
    "Marco": 431232131,
    "Mina": 767767676
}
print(phonebook2)

# Iterate on dictionary
for name, number in phonebook.items():
    print("Phone num of %s is %d" % (name, number))

# Delete from dictionary
del phonebook2["Marco"]
print(phonebook2)

phonebook.pop("Sarah")
print(phonebook)

if "Jake" in phonebook:
    print("Jake already exists")
else:
    phonebook["Jake"] = 8988998999
    print(phonebook)