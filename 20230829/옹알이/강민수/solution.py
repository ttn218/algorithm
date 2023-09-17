pron = [
    "aya", "ye", "woo", "ma"
]

def isBabbl(babbl):
    if len(babbl) == 0: return True
    for p in pron:
        if babbl[0:len(p)] == p: return isBabbl(babbl[len(p):])
    
    return False

def solution(babbling):
    answer = 0
    
    for babbl in babbling:
        if isBabbl(babbl): answer += 1
    
    return answer