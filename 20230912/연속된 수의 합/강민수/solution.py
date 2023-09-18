def solution(num, total):
    start = 0
    
    while True:
        answer = []
        total2 = 0
        for i in range(start, start + num):
            answer.append(i)
            total2 += i
            
        if total2 < total:
            start += 1
        elif total2 > total:
            start -= 1
        else:
            return answer
