import math 
idx_to_skip = 0 
result_list = []
while len(nums) > idx_to_skip:
    product_list = nums[:idx_to_skip] + nums[idx_to_skip+1:]
    result = math.prod(product_list)
    result_list.append(result)
    idx_to_skip +=1
print(result_list)


