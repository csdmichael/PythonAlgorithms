class Solution:
    def stringToInt(s: str) -> int:
        isNegative = False
        resDigits = ""
        digits = ['0','1','2','3','4','5','6','7','8','9']

        for char in s:
            if len(resDigits) == 0:
                if char == '-':
                    isNegative = True
                else:
                    if char == " " or char == "+":
                        continue
                    else:
                        if char in digits:
                            resDigits = str(char)
                        else:
                            break
            else:
                if char in digits:
                    resDigits += str(char)
                else:
                    break
                print(resDigits)
        if resDigits == "":
            resDigits = "0"
        res = int(resDigits)
        if res > 2147483648:
            res = 2147483648
        if (isNegative):
            res *= -1
        
        return res
    
y = Solution.stringToInt("0-1")
print(y)