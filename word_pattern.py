def wordPattern(pattern, s):
    res=True

    sent=s.split(" ")

    pat_dict={}

    if len(pattern)!=len(sent):
        print("came here")
        return False

    for i in range(0, len(pattern)):

        if pattern[i] in pat_dict:
           if pat_dict[pattern[i]]!=sent[i]:
               #print("came here")
               return False
        else:
            if sent[i] in pat_dict.values():
                return False
            else:
                pat_dict[pattern[i]]=sent[i]
    #print("came here")
    return res

pattern = "abba"
s = "dog dog dog dog"

print(wordPattern(pattern, s))