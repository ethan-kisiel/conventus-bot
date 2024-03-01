"""
Models which do not require the usage of a sql database
"""

from datetime import datetime


class MeetingSlot:
    """
    Contains the information for a single meeting slot
    """

    start_time: datetime

    def __init__(self, data: dict):
        # start_time = decode datetime
        pass

    @property
    def as_dict(self):
        """
        Returs this object as a dictionary
        """
        pass


class MeetingSchedule:
    """
    Contains the schedule information for meetings
    """

    # the number of minutes until this meeting is considered finished
    meeting_length: int
    notification_delta: int  # minutes before meeting time to send the notif
    meetings: list[MeetingSlot]

    def __init__(self, data: dict):
        pass

    @property
    def as_dict(self):
        """
        Returs this object as a dictionary
        """
        pass
