atoms = {
    "zero": 0,
    "one": 1, 
    "two": 2, 
    "three": 3, 
    "four": 4, 
    "five": 5, 
    "six": 6, 
    "seven": 7, 
    "eight": 8, 
    "nine": 9
}

def solution(numbers):
    answer = 0

    for atomkey, value in atoms.items():
        numbers = numbers.replace(atomkey, str(value))
    
    answer = int(numbers)
    
    return answer