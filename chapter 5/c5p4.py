s = set()
s.add(20)
s.add(20.0)
s.add('20') # length of s after these operations?
print(len(s)) #  2 answer isliye diya bcz 20 and 20.0 are considered equal in Python, so they are treated as the same element in the set. The string '20' is a different type, so it is counted as a separate element. Therefore, the length of the set is 2.