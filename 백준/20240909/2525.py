now = input()
time = int(input())

hour, minute = now.split(' ')

hour = int(hour)
minute = int(minute)

time_h = int(time / 60)
time_m = time % 60

minute += time_m

if minute > 59:
    minute -= 60
    hour +=1

hour += time_h

if hour > 23:
    hour -= 24

print(f'{hour} {minute}')
