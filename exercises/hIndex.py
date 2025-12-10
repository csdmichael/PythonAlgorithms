def getHIndex(citations: list[int]) -> int:
    citations.sort(reverse=True)
    print(citations)
    h = 0
    for i in range(len(citations)):
        if citations[i] <= i + 1:
            print(f'i={i}, citation={citations[i]}')
            return i + 1
    return h

'''
[3,2,1,1,0]

3
2 --> i + 1
1
1
0
'''

def getHIndexOptimized(citations: list[int]) -> int:
    n = len(citations)
    counts = [0] * n
    print(counts)
    for i in range(len(citations)):
        c = citations[i]
        if c > n - 1:
            counts[n-1] += 1
        else:
            counts[c] += 1
    print(counts)

    h = 0
    for i in range(n - 1, -1, -1):
        print(f"i={i}")
        if counts[i] + h <= i:
            h += counts[i]
        else:
            break

    return h


'''
[3,2,1,1,0]

[1,2,1,1,0]
           <---------
'''

y = getHIndexOptimized([3,0,6,1,5])
print(y)

