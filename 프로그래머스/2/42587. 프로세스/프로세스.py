def solution(priorities, location):
    queue = [(p, i) for i, p in enumerate(priorities)]
    count = 0

    while queue:
        p, i = queue.pop(0)

        if any(other > p for other, _ in queue):
            queue.append((p, i))
        else:
            count += 1
            if i == location:
                return count
