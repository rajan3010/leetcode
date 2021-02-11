state_dict={}
reverse_state_dict={}

def nextDay(bitmap):
    res=~((bitmap<<1)^(bitmap>>1))
    res=res&(0x7e)
    return res

def prisonAfterNdays(cells, N):

    bitmap=0x0

    #create bitmap first
    for i in cells:
        bitmap<<=1
        bitmap|=i

    j=0
    prev_index=0

    while j<=(N-1):
        #print("first while")
        if bitmap not in state_dict:
            state_dict[bitmap]=j
            reverse_state_dict[j]=bitmap
            prev_index=j
            j=j+1
            bitmap=nextDay(bitmap)

        else:
            cur_ind=state_dict[bitmap]
            cycle_len=prev_index-cur_ind+1
            final_ind=cur_ind+((N-j)%cycle_len)
            #print(reverse_state_dict)
            #print(state_dict)
            bitmap=reverse_state_dict[final_ind]
            break
    
    k=0
    res=[]
    print(bin(bitmap))
    while k<8:
        #print("second while")
        bit=bitmap&(0x1)
        res.append(bit)
        bitmap>>=1
        k+=1

    return res[::-1]


cells = [1,0,0,1,0,0,1,0]
N = 1000000000
print(prisonAfterNdays(cells, N))





    