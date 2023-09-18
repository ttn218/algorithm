def solution(before, after):
    
    for atom in after:
        index = before.find(atom)
        
        if index > -1:
            before = before.replace(atom, '', 1)
        else:
            return 0
    return 1
