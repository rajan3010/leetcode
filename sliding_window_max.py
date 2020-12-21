def slidingWindowMax(nums, k):

    n= len(nums)
    if n*k==0:
        return []
    if k==1:
        return nums

    left=[0]*len(nums) # maintain left array to store sliding maximum from left-> right
    right=[0]*len(nums) #maitain right window to store sliding maximum from right->left
    left[0]=nums[0]
    right[0]=nums[n-1]
    res=[]

    for i in range(1,n):
        pass
        if i%k==0:
            left[i]=nums[i]
        else:
            left[i]=max(left[i-1],nums[i])

        j=n-i-1
        if (j+1)%k==0:
            right[j]=nums[j]
        else:
            right[j]=max(right[j+1],nums[j])

    for i in range(k-1, n):
        res.append(max(left[i],right[i-k+1]))

    return res

nums = [9,11]
k = 2
print(slidingWindowMax(nums, k))