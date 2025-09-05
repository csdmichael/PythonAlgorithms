from typing import List


class Distrib:
    def mean(arr:List[int]):
        return sum(arr) / len(arr)
    
    def median(arr:List[int]):
        arr.sort()
        n = len(arr)
        mid = n // 2
        if n % 2 == 0:
            return (arr[mid - 1] + arr[mid]) / 2
        else:
            return arr[mid]
        
    def mode(arr:List[int]):
        frequency = {}
        for num in arr:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1
        max_freq = max(frequency.values())
        modes = [num for num, freq in frequency.items() if freq == max_freq]
        return modes[0] if len(modes) == 1 else modes
    
    def stddev(arr:List[int]):
        mean_value = Distrib.mean(arr)
        variance = sum((x - mean_value) ** 2 for x in arr) / len(arr)
        return variance ** 0.5

# Example usage:
data = [0, 4, 9, 6, 7, 4, 3]
print("Mean:", Distrib.mean(data))
print("Median:", Distrib.median(data))
print("Mode:", Distrib.mode(data))
print("Standard Deviation:", Distrib.stddev(data))
