import math

def get_minutes_degrees(minutes : int):
    minute_degrees = (minutes * 6)
    return minute_degrees

def get_hours_degrees(hours : int, minutes : int):
    hours_degrees = (hours % 12) * 30
    hours_degrees = hours_degrees + minutes * 0.5
    return hours_degrees

def get_total_angle(hours : int, minutes : int):
    total_angle = math.fabs(get_hours_degrees(hours, minutes) - get_minutes_degrees(minutes))
    return total_angle



print(get_total_angle(9,49))