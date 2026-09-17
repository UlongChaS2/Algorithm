def solution(nums):
    dic = {}
    for num in nums:
        if num in dic:
            dic[num] += 1
        else:
            dic[num] = 1
            
    return min(len(nums) // 2, len(dic.keys()))
    