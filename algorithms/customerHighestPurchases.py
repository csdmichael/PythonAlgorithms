purchases = [
    ["Mike", 50],
    ["Sarah", 60],
    ["John", 20],
    ["Mike", 70]
]

custs = {}

max = 0
for i in range(len(purchases)):
    key = purchases[i][0]
    if key in custs:
        print(f"{key} exists")
        custs[key] += purchases[i][1]
    else:
        custs[key] = purchases[i][1]
    if (custs[key] > max):
        max = custs[key]
print(custs)
print(f"Max: {max}")