
import datetime as dt
print(dt.datetime.now())

import datetime
start_time = datetime.datetime.now()
print(start_time.replace(month = 12, day = 25))

#남은시간 구하기
import datetime as dt
today = dt.date.today()
print('오늘은 {}년 {}월 {}일입니다'.format(today.year, today.month, today.day))
xMas = dt.datetime(2026, 12, 25)
time_gap = xMas - dt.datetime.now()
print('다음 크리스마스까지는 {}일 {}시간 남았습니다.'.format(\
    time_gap.days,time_gap.seconds // 3600))
