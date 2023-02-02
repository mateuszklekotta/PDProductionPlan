def convert(date, time, hours):
    import pandas as pd
    days_offset = hours // 8
    hours_offset = (hours % 8)*3600
    print(hours_offset)
    fin_time = 0
    if time + hours_offset > 54000:
        fin_time = 25200 + time + hours_offset - 54000
        days_offset += 1
    else:
        fin_time = time + hours_offset
    return[0, fin_time]


print(convert(1, 49020, 5))
