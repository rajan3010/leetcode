from collections import defaultdict

def getBitMask(word):
    mask=0

    for i in word:
        #Set the bit of the letter index to 1
        ind=ord(i)-ord('a')
        mask|=1<<ind
    
    #Return the bit mask
    return mask

def findNumofValidWords(words, puzzles):

    bitmask_freq_map=defaultdict(int)

    for word in words:

        #get bitmask and map to maintain the frequency
        mask=getBitMask(word)
        bitmask_freq_map[mask]=bitmask_freq_map[mask]+1

    total=[0]*len(puzzles)
    for i,puzzle in enumerate(puzzles):

        #for each puzzle get the mask 
        puz_mask=submask=getBitMask(puzzle)
        #get the first letter
        first_letter_ind=ord(puzzle[0])-ord('a')


        #loop till the submask combination becomes 0, which means all permutations are over
        while submask!=0:
        #if the first letter of puzzle is found in the submask bitmap
            if (submask>>first_letter_ind)&1:
        #Increment the count by the number of words with that bitmap mapping
                total[i]+=bitmask_freq_map[submask]
        #evaluate the next sub combination
            submask=(submask-1)&puz_mask

    return total

words = ["aaaa","asas","able","ability","actt","actor","access"]
puzzles = ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]

print(findNumofValidWords(words, puzzles))