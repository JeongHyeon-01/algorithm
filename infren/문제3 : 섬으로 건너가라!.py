wait = 14000605
#1200202

'''
시간        인원   누적
9          25    25
9 10       15    40
9 20       15    55
9 30       15    70
9 40       15    85
9 50       15    100

1시간에 100 12시간 1200 명
'''
import datetime
def solution(waiting):
    year_day = 0
    for i in range(1,11):
        year_day += 2**i
    year = (waiting//1200) // year_day
    extra_date = (waiting//1200) % year_day

    monthdate = 0
    month = 0
    for i in range(1,11):
        minusdate = monthdate
        monthdate += 2**i
        month +=1
        if monthdate > extra_date:
            break
    day = extra_date - minusdate
    last_wait_people = waiting % 1200
    time = last_wait_people // 100 +9
    start_min = [25,40,55,70,85,100]
    target_min_people = last_wait_people % 100+1
    for i in start_min:
        if i> target_min_people:
            min = start_min.index(i)*10
            break
    if datetime.datetime.minute + min >60:
        min = (datetime.datetime.minute+min) -60

    return year, month, day , time, min

print(solution(wait))