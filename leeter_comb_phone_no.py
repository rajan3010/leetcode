def letterCombinations(digits):

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
print(letterCombinations(input))
