from datetime import datetime


def convert_time_to_string(dt: datetime) -> str:
    return f"{dt.hour}:{dt.minute}"


def time_has_changed(prev_time: datetime) -> bool:
    return convert_time_to_string(datetime.now()) != convert_time_to_string(prev_time)
