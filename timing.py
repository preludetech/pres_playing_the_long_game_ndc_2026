timing = """
intro 
"""


def parse_time(time_str):
    minutes, seconds = map(int, time_str.split(':'))
    return minutes * 60 + seconds

total_seconds = 0
for line in timing.strip().split('\n'):
    if line.strip():
        time_part = line.split()[-1]
        total_seconds += parse_time(time_part)

total_minutes = total_seconds // 60
remaining_seconds = total_seconds % 60

print(f"total time = {total_minutes}:{remaining_seconds:02d}")