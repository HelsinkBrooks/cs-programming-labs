time_seconds = int(input())
time_hours = time_seconds // 3600
time_minutes = (time_seconds % 3600) // 60 % 60
time_seconds_result = time_seconds % 60

print(f'{time_hours:02d}:{time_minutes:02d}:{time_seconds_result:02d}')