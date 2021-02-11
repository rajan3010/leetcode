from collections import defaultdict
def group_anagram(strs):

    n=len(strs)

    anagram_dict=defaultdict(list)
    res=[]

    for i in range(n):
        
        sorted_str=tuple(sorted(strs[i]))
        anagram_dict[sorted_str].append(strs[i])

    for key in anagram_dict:
        if anagram_dict[key]:
            res.append(anagram_dict[key])

    return res

strs = ["eat","tea","tan","ate","nat","bat"]
print(group_anagram(strs))

        

