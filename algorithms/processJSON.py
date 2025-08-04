import json

class JSONOperations:
    def __init__(self, jsonVal):
        self.jsonVal = json.loads(jsonVal)

    def GetString(self) -> str:
        s = json.dumps(self.jsonVal) 
        print(s)
        return s

    def GetSalesTotal(self) -> str:
        sales = self.jsonVal["Sales"]
        x = 0
        for sale in sales:
            print("Amount", sale["Amount"])
            x += sale["Amount"]
        
        return x

input = """{"Sales": [
    {"TxnDate":"2025-01-01", "Customer": "Mike", "Amount": 10},
    {"TxnDate":"2025-02-02", "Customer": "John", "Amount": 20}
]}"""
j = JSONOperations(
    input
)

j.GetString()
y = j.GetSalesTotal()
print("Sales Total", y)