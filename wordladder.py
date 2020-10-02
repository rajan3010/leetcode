from collections import defaultdict
from collections import deque

wordmap=defaultdict(list)

def preprocess(wordList):

    L= len(wordList[0])
    for word in wordList:
        for i in range(L):
            intermediate=word[:i]+"*"+word[i+1:]
            wordmap[intermediate].append(word)

def ladderlength(beginWord, endWord, wordList):

    preprocess(wordList)

    L=len(beginWord)

    queue=deque([(beginWord, 1)])

    visited={beginWord: True}

    if endWord not in wordList or not endWord or not beginWord or not wordList:
        return 0

    while queue:
        curr_word, level=queue.popleft()

        for i in range(L):
            curr_inter=curr_word[:i]+"*"+curr_word[i+1:]
            potential_list=wordmap[curr_inter]
            for word in potential_list:
                if word not in visited:
                    visited[word]=True

                    if word==endWord:
                        print(word)
                        return level+1
                    else:
                        queue.append((word,level+1))
    return 0

print(ladderlength("hot", "dog", ["hot", "dog"]))