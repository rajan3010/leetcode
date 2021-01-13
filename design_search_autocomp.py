from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.child=defaultdict(TrieNode)
        self.isWord=False
        self.word=""
        self.hits=0

class Trie:
    def __init__(self):
        self.root_node=TrieNode()
    
    def insert(self, sentence, hits=1):

        cur_node=self.root_node
        for ch in sentence:
            cur_node=cur_node.child[ch]
        
        if not cur_node.isWord:
            cur_node.isWord=True
            cur_node.word=sentence
            cur_node.hits=hits
        else:
            cur_node.hits+=1

    def search(self, char):

        curr_node=self.root_node
        dic={}
        res=[]

        #print(curr_node.child)
        for ch in char:
            #print(ch)
            if ch not in curr_node.child:
                return None
            curr_node=curr_node.child[ch]
            #print(curr_node.child)

        stack=[curr_node]

        while stack:
            node=stack.pop()

            if node.isWord:
                dic[node.word]=node.hits 
            
            children=node.child

            for child_node in children:
                stack.append(node.child[child_node])

        i=3
        #print(dic)
        for word, hits in sorted(dic.items(), key=lambda x:(-x[1], x[0])):
            if i==0:
                break
            res.append(word)
            i=i-1

        return res

class AutocompleteSystem:
    def __init__(self, sentences, times):
        self.inp=""
        self.trie_ds=Trie()

        for sentence, time in zip(sentences, times):
            self.trie_ds.insert(sentence, time)

    def input(self, c):
        if c=="#":
            self.trie_ds.insert(self.inp)
            self.inp=""
            return []
        self.inp+=c
        return self.trie_ds.search(self.inp)

a=AutocompleteSystem(["i love you", "island","ironman", "i love leetcode"], [5,3,2,2])
print(a.input('i'))
print(a.input(' '))
print(a.input('#'))