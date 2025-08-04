sum  = lambda x, y : x + y
#def sum(x,y):
#    return x + y

c = sum(5,6)
print(c)

l = [2,4,7,3,14,19]
for i in l:
    isOdd = lambda x : (x % 2) == 1
    print(i, isOdd(i))