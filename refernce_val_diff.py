def ref_test(n):
    n[0]+=1
    print("n inside: ",n)

n=[1]
ref_test(n)
print("n outside: ", n)