def foo(first, second, third, *therest):
    print("First: %s" % first)
    print("Second: %s" % second)
    print("Third: %s" % third)
    print("Rest: %s" % list(therest))

foo("as", "bs", "cs", 5, 6, 7, "abc")


def bar(first, second, third, **options):
    if options.get("action") == "sum":
        print("The sum is: %d" %(first + second + third))

    if options.get("number") == "first":
        return first

result = bar(1, 2, 3, action = "sum", number = "first")
print("Result: %d" %(result))

def passParamsAnyOrder(a,b, **params):

    if params.get("operator") == "+":
        x = a + b
    if params.get("operator") == "-":
        x = a - b
    
    if params.get("choice") == "first":
        return x, a
    
    if params.get("choice") == "second":
        return x, b
    
ans = passParamsAnyOrder(5, 6, operator = "+", choice = "second")
print(ans)