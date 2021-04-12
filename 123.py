def isAnagram(s1,s2):
    if len(s1) != len(s2):
        return "is not an anagram"
    else:
        l1, l2 = [], []
        for i in range(len(s1)):
            l1.append(s1[i])
            l2.append(s2[i])
        l1.sort()
        l2.sort()
        if l1 == l2:
            return "is an anagram"
        else:
            return "is not an anagram"

s1,s2 = input("Please enter two letter separated by space: ").split()
print(isAnagram(s1, s2))