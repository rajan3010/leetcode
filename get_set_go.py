# The function is expected to return BOOLEAN.
# The function accepts following parameters:
# 1. INTEGER_ARRAY calCounts
# 2. INTEGER requiredCals

def isSubsetSum(calCount,requiredCals):
    n =len(calCount)   
    subset=([[False for i in range(requiredCals+1)] for i in range(n+1)])
  
# If sum is 0, then answer is true cause no need to take any food item
    for i in range(n+1):
        subset[i][0] = True
  
# If sum is not 0 and there is no food item,
# then answer is false
    for i in range(1,requiredCals+1):
        subset[0][i]=False
  
# Fill the subset table in botton up manner
    for i in range(1,n+1):
        for j in range(1,requiredCals+1):
#case when jth food item's calory isgreater than requiredCals
#the we exclude to add in subset
            if j<calCount[i-1]:
                subset[i][j] = subset[i-1][j]
#case when jth food item's calory is greater than requiredCals
#the we include to add in subset
            if j>=calCount[i-1]:
                subset[i][j] = (subset[i-1][j] or subset[i - 1][j-calCount[i-1]])
    return subset[n][requiredCals]
  

input_ = [2,9,5,1,6]
x = 12

print(isSubsetSum(input_, x))