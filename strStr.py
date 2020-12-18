def strStr(word, needle):
    nL, wL= len(needle), len(word)

    if nL==0:
        return 0

    word_ptr=0 #initial popinter for word

    while word_ptr<(wL-nL+1):

        while word_ptr<(wL-nL+1) and word[word_ptr]!=needle[0]:
            word_ptr+=1

        curr_len=needle_ptr=0

        while word_ptr<wL and needle_ptr<nL and word[word_ptr]==needle[needle_ptr]:
            word_ptr+=1
            needle_ptr+=1
            curr_len+=1

        if curr_len==nL:
            return word_ptr-curr_len
        else:
            word_ptr=word_ptr-curr_len+1
    
    return -1

haystack ="masturbate"
needle = "turb"
print(strStr(haystack, needle))