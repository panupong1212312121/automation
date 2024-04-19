from pathlib import Path
import calendar
month_names = list(calendar.month_name[1:])
days = ['Day 1','Day 10','Day 20','Day 30']
for i, month in enumerate(month_names):
    for day in days:
        Path (f'./File Managment/2024/{i+1}.{month}/{day}').mkdir(parents=True,exist_ok=True)