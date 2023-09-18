
def solution(park, routes):
    answer = [0, 0]
    
    for i, p in enumerate(park):
        index = p.find('S')
        if index >= 0:
            answer = [i, index]
    
    width = len(park[0])
    height = len(park)
    
    for route in routes:
        direction, distance = route.split(' ')
        
        distance = int(distance)
        
        for i in range(distance + 1):
            i = i
            
            if direction == 'E':
                if answer[1] + i > width - 1 or park[answer[0]][answer[1] + i] == 'X':
                    break
            elif direction == 'S':
                if answer[0] + i > height - 1 or park[answer[0]+ i][answer[1]] == 'X':
                    break
            elif direction == 'W':
                if answer[1] - i < 0 or park[answer[0]][answer[1] - i] == 'X':
                    break
            elif direction == 'N':
                if answer[0] - i < 0 or park[answer[0] - i][answer[1]] == 'X':
                    break
            
            if i == distance:
                if direction == 'E':
                    answer[1] += distance
                elif direction == 'S':
                    answer[0] += distance
                elif direction == 'W':
                    answer[1] -= distance
                elif direction == 'N':
                    answer[0] -= distance
    
    return answer