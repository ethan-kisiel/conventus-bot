"""
Contains the constants for the base system
"""

from enum import Enum


class Weekday(Enum):
    """
    enum for weekdays
    """

    SUNDAY = "Sun"
    MONDAY = "Mon"
    TUESDAY = "Tues"
    WEDNESDAY = "Wed"
    THURSDAY = "Thur"
    FRIDAY = "Fri"
    SATURDAY = "Sat"


class TableName(Enum):
    """Table names for sqlalchemy classes"""

    MEETING = "meetings"
    TASK = "tasks"
    NOTE = "notes"
    FEATURE = "features"
    USER = "users"

    USER_MEETING_ASSOCIATION = "users_meetings"
    USER_TASK_ASSOCIATION = "users_tasks"
