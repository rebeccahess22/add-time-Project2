def add_time(start, duration, start_day=None):
    # Map days to indexes
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    day_to_index = {day.lower(): i for i, day in enumerate(days_of_week)}

    # Parse start time
    start_hour, start_min = map(int, start.split()[0].split(':'))
    period = start.split()[1]

    # Convert start to 24-hour format
    if period == 'PM' and start_hour != 12:
        start_hour += 12
    elif period == 'AM' and start_hour == 12:
        start_hour = 0

    # Parse duration by applying the integer function to hours and minutes
    dur_hour, dur_min = map(int, duration.split(':'))

    # Total minutes and calculate new hour/minute
    total_minutes = start_hour * 60 + start_min + dur_hour * 60 + dur_min
    new_hour_24 = (total_minutes // 60) % 24
    new_minute = total_minutes % 60
    days_later = total_minutes // (24 * 60)

    # Determine new period and 12-hour format
    new_period = 'AM' if new_hour_24 < 12 else 'PM'
    new_hour_12 = new_hour_24 % 12
    new_hour_12 = 12 if new_hour_12 == 0 else new_hour_12

    # Calculate new day if provided
    if start_day:
        start_day_index = day_to_index[start_day.lower()]
        new_day_index = (start_day_index + days_later) % 7
        new_day = days_of_week[new_day_index]
        day_part = f", {new_day}"
    else:
        day_part = ""

    # Format days later message
    if days_later == 0:
        later_msg = ""
    elif days_later == 1:
        later_msg = " (next day)"
    else:
        later_msg = f" ({days_later} days later)"

    # Format final time
    new_time = f"{new_hour_12}:{str(new_minute).zfill(2)} {new_period}{day_part}{later_msg}"
    
    return new_time

add_time('3:30 PM', '2:12')
add_time('11:55 AM', '3:12')
add_time('2:59 AM', '24:00')
add_time('11:59 PM', '24:05')
add_time('8:16 PM', '466:02')
add_time('3:30 PM', '2:12', 'Monday')
add_time('2:59 AM', '24:00', 'saturDay')
add_time('11:59 PM', '24:05', 'Wednesday')
add_time('8:16 PM', '466:02', 'tuesday') 