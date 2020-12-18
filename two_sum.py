def twoSum(nums, target):
    comp_dict={}

    for i in range(0, len(nums)):

        comp=target-nums[i]
        if comp in comp_dict:
            return [comp_dict[comp], i]
        comp_dict[nums[i]]=i

    return -1

nums = [3,2,4]
target = 6

print(twoSum(nums, target))