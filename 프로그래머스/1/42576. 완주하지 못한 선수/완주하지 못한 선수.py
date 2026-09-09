def solution(participant, completion):
    dic = {}
    for p in participant:
        dic[p] = dic.get(p, 0) + 1
            
    for p in completion:
        dic[p] -= 1
    
    for name, cnt in dic.items():
    	if cnt == 1:
        	return name