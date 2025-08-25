from typing import List

class Solution:
    def classifyPeopleByFriendsCount(arr: List[List[int]], X: int) -> List[List[int]]:
        res = [[],[]]
        if arr == None:
            return res
        
        hashMap = {}
        rows = len(arr)

        for i in range(rows):
            person1 = arr[i][0]
            person2 = arr[i][1]
            val = arr[i][2]
            incr = 1
            if val == 'Unfriend':
                incr *= -1
            if person1 in hashMap:
                hashMap[person1] += incr
            else:
                hashMap[person1] = incr

            if person2 in hashMap:
                hashMap[person2] += incr
            else:
                hashMap[person2] = incr

            print(hashMap)

        for key, val in hashMap.items():
            if val < X:
                res[0].append(key)
            else:
                res[1].append(key)
        return res

input = [
    ['X', 'Y', 'Friend'],
    ['X', 'Z', 'Friend'],
    ['X', 'Y', 'Unfriend'],
    ['Y', 'Z', 'Friend']
]

y = Solution.classifyPeopleByFriendsCount(input, 2)
print(y)

'''
X: 1 
Y: 1
Z: 2

Output at 2 or more friends = [['X', 'Y'], ['Z']]
'''