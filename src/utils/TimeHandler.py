from src.constants.Constants import SettingConstants

from datetime import datetime


def get_current_time():
    return datetime.utcnow()


def get_current_time_string():
    return get_current_time().strftime(SettingConstants().get_time_format())


def get_datetime_from_string(string):
    return datetime.strptime(string, SettingConstants().get_time_format())
