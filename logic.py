from config import SCHEDULE_PATH

def get_schedule_for_monday():
    return format_schedule(SCHEDULE_PATH.get("monday", "Расписание на понедельник не найдено."))

def get_schedule_for_tuesday():
    return format_schedule(SCHEDULE_PATH.get("tuesday", "Расписание на вторник не найдено."))

def get_schedule_for_wednesday():
    return format_schedule(SCHEDULE_PATH.get("wednesday", "Расписание на среду не найдено."))

def get_schedule_for_thursday():
    return format_schedule(SCHEDULE_PATH.get("thursday", "Расписание на четверг не найдено."))

def get_schedule_for_friday():
    return format_schedule(SCHEDULE_PATH.get("friday", "Расписание на пятницу не найдено."))

def format_schedule(schedule):
    if isinstance(schedule, dict):
        return "\n".join([f"{time}: {lesson}" for time, lesson in schedule.items()])
    return schedule