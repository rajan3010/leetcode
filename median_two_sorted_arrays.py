def findMedianSortedArrays(nums1, nums2):

    m= len(nums1)
    n=len(nums2)

    if n<m:
        temp=nums1
        nums1=nums2
        nums2=temp
        m= len(nums1)
        n=len(nums2)

    low=0
    high=m
    median=0


    while (low<=high):
        nums1_part=(low+high)//2
        nums2_part=((m+n+1)//2)-nums1_part #since nums1_part + nums2_part must logically be equal to total array partitian

        max_Lx=float('-inf') if nums1_part==0 else nums1[nums1_part-1]
        max_Ly=float('-inf') if nums2_part==0 else nums2[nums2_part-1]
        min_Rx=float('inf') if nums1_part==m else nums1[nums1_part]
        min_Ry=float('inf') if nums2_part==n else nums2[nums2_part]

        if max_Lx<=min_Ry and max_Ly<=min_Rx:
            if (m+n)%2==0:
                return (max(max_Lx, max_Ly)+min(min_Rx,min_Ry))/2
            else:
                return max(max_Lx, max_Ly)
        
        elif max_Lx>min_Ry:
            high=nums1_part-1
        else:
            low=nums1_part+1

nums1 = [1,3]
nums2 = [2]

print(findMedianSortedArrays(nums1,nums2))


