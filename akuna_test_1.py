def sortString(s):
    s = list(s)
    result = ''
    prev=''
    while s:
        for letter in sorted(set(s)):
            s.remove(letter)
            result += letter
            prev=letter
        for letter in sorted(set(s), reverse=True):
            s.remove(letter)
            result += letter
    return result

input='aaazzz'
print(sortString(input))