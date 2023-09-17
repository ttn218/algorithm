from datetime import date

def solution(date1, date2):
    date_1 = date(year=date1[0], month=date1[1], day=date1[2])
    date_2 = date(year=date2[0], month=date2[1], day=date2[2])
    if date_1 < date_2:
        return 1
    
    return 0