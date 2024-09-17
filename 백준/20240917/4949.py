
def isMate(word1, word2):
    if word1 == '(' and word2 == ')':
        return True
    if word1 == '[' and word2 == ']':
        return True
    return False

while True:
    line = input()
    if line == '.':
        break
    
    stack = []
    for c in line:
        if c == '(' or c == ')' or c == '[' or c == ']':
            if len(stack) == 0:
                stack.append(c)
            elif isMate(stack[-1], c):
                stack.pop()
            else:
                stack.append(c)
    
    if len(stack) > 0:
        print('no')
    else:
        print('yes')
        
