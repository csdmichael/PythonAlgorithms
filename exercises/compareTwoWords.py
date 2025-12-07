def areWordsSimilar(firstWord: str, secondWord: str) -> bool:
    if firstWord == None or secondWord == None:
        return False
    
    if len(firstWord) != len(secondWord):
        return False
    
    firstWord = firstWord.lower()
    secondWord = secondWord.lower()

    hash = {}

    # Put chars of first word in hash table - Key is char and value is num of occurences
    for c in firstWord:
        if c in hash:
            hash[c] += 1
        else:
            hash[c] = 1

    for c in secondWord:
        if c not in hash:
            return False
        else:
            hash[c] -= 1
            if hash[c] == 0:
                del hash[c]

    if len(hash) == 0:
        return True
    else:
        return False
    
ans = areWordsSimilar('Hello', 'hello')

print(ans)