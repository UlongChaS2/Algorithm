def solution(nums):
    # 무조건 해시 == object라는 생각으로 1 더했었는데 value는 사용을 안했었음
    return min(len(nums) // 2, len(set(nums)))
    