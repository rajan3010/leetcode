def partitionLabels(S):

    last_hash={c:ind for ind,c in enumerate(S)}

    part_last=part_start=0

    res=[]

    for i,ch in enumerate(S):

        part_last=max(part_last,last_hash[ch])

        if i==part_last:
            l=part_last-part_start+1
            res.append(l)
            part_start=i+1

    return res

S = "ababcbacadefegdehijhklij"
print(partitionLabels(S))