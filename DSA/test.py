from typing import Counter


s = [1,1,2,2,3,3,3,3]

hashtable = Counter(s)
print(list(hashtable.values()))