'''def letterCombinations(digits):

    phone_no={
        "2":['a','b','c'],
        "3":['d','e','f'],
        "4":['g','h','i'],
        "5":['j','k','l'],
        "6":['m','n','o'],
        "7":['p','q','r'],
        "8":['s','t','u','v'],
        "9":['w','x','y','z']
        }
    res=[]

    def backtrack(combinations, digits):

        if len(digits)==0:
            res.append(combinations)
        else:    
            for char in phone_no[digits[0]]:
                backtrack(combinations+char, digits[1:])

    backtrack("", digits)

    return res

input=""
print(letterCombinations(input))'''

'''def pairSummingTwo(x):
    n=len(x)
    res=[]

    for i in range(0,7):
        target=2**i
        comp_dict={}

        for j in range(n):

            comp=target-x[j]

            if comp in comp_dict:
                res.append((comp, x[j]))
            elif (2*x[j]==target):
                res.append((x[j], x[j]))
            comp_dict[x[j]]=j

    print(res)
    return len(res)'''

'''def almostSubstring(t,s):

    ret=0

    for i in range(0,len(t)-4):
        if (t[i]+t[i+2]+t[i+4])==s:
            ret+=1
    
    return ret

t="azcabcab"
s="acb"

print(almostSubstring(t, s))'''

'''def text_editor(operations):
    command=""
    param=""
    text=""
    undo_stack=[]
    text_copy=""

    for op in operations:
        try:
            command, param=op.split(" ")
        except:
            command=op

        if command=="INSERT":
            undo_stack.append(text)
            text=text+param
        elif command=="DELETE":
            if text!="":
                undo_stack.append(text)
                text=text[:-1]
        elif command=="COPY":
            ind=int(param)

            if ind<len(text):
                text_copy=text[ind:]
            else:
                text_copy=""
        elif command=="PASTE":
            if text_copy!="":
                undo_stack.append(text)
                text=text+text_copy
        
        elif command=="UNDO":
            text=undo_stack.pop()
    
    return text

print(text_editor(["INSERT Da","COPY 0", "UNDO", "PASTE", "PASTE", "COPY 2", "PASTE", "PASTE", "DELETE", "INSERT aaam"]))
'''

def restore(pairs):

    neighbor={}
    res=[]

    for n1, n2 in pairs:
        if n1 not in neighbor:
            neighbor[n2]=[n1, n2]
        else:
            neighbor[n2]=neighbor[n1]+[n2]
            res=neighbor[n2]

    return res

print(restore([[3,5],[1,5],[1,4],[4,2]]))        



