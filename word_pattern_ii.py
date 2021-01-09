def wordPatternSecond(pattern, s):

    dict_={}
    rev_dict={}

    return backtrack_wp(pattern, s, dict_, rev_dict)

def backtrack_wp(pattern, s, dict_, rev_dict):

    if len(pattern)==0 and len(s)>0:
        return False
        
    if len(pattern)==len(s)==0:
        return True

    for end in range(1,len(s)-len(pattern)+2):
        if pattern[0] not in dict_ and s[:end] not  in rev_dict:
            dict_[pattern[0]]=s[:end]
            rev_dict[s[:end]]=pattern[0]

            if backtrack_wp(pattern[1:], s[end:], dict_, rev_dict):
                return True
            del dict_[pattern[0]]
            del rev_dict[s[:end]]
            
        elif pattern[0] in dict_ and dict_[pattern[0]]==s[:end]:
            if backtrack_wp(pattern[1:],s[end:], dict_, rev_dict):
                return True

    return False

pattern = "aaaa"
s = "asdasdasdasd"
print(wordPatternSecond(pattern, s))