def add_time(start, duration, day=None):
    
    # Time converter for further calculation
    def convert_to_24_hour(hour, minute, meridian):
        if meridian == "PM" and hour != 12:
            hour += 12
        elif meridian == "AM" and hour == 12:
            hour = 0
        return hour, minute
    
    def convert_to_12_hour(hour, minute):
        meridian = "AM" if hour < 12 else "PM"
        hour = hour if hour % 12 != 0 else 12
        hour = hour if hour <= 12 else hour - 12
        return hour, minute, meridian
    
    # Parse start time (ex: '11:43 AM')
    start_time, meridian = start.split()
    start_hour, start_minute = map(int, start_time.split(':'))
    start_hour, start_minute = convert_to_24_hour(start_hour, start_minute, meridian)
    
    # Parse duration time
    duration_hour, duration_minute = map(int, duration.split(':'))
    
    # Calculate result (duration + start time)
    total_minutes = start_minute + duration_minute
    extra_hours = total_minutes // 60
    new_minute = total_minutes % 60
    
    total_hours = start_hour + duration_hour + extra_hours
    new_hour = total_hours % 24
    days_later = total_hours // 24
    
    # Convert result to 12-hour format
    new_hour, new_minute, new_meridian = convert_to_12_hour(new_hour, new_minute)
    
    # Determine the new day of the week if given
    days_of_week = ["Sunday", "Monday", 
                    "Tuesday", "Wednesday", 
                    "Thursday", "Friday", 
                    "Saturday"
                    ]
    if day:
        day = day.capitalize()
        day_index = days_of_week.index(day)
        new_day = days_of_week[(day_index + days_later) % 7]
    
    # If result is next day (result - duration = 1)
    next_day_text = " (next day)" if days_later == 1 else ""
    
    # If result is n days later (result - duration > 1)
    days_later_text = f" ({days_later} days later)" if days_later > 1 else ""
    
    # Return correct format
    new_time = f"{new_hour}:{new_minute:02d} {new_meridian}"
    if day:
        new_time += f", {new_day}"
    new_time += next_day_text + days_later_text
    
    return new_time
