import itertools
from datetime import date, time, datetime, timedelta 
"""
This is a standard (built-in) library for dealing with times (allows addition of times and stuff) and also deals with daylight savings.

datetime(2026, 11, 10, 9, 0)   # "9am 2026 10th Nov"

In cases where we need to account for daylight savings etc. follow this pattern:

from zoneinfo import ZoneInfo (included with icalendar)
UK = ZoneInfo("Europe/London")

date = dateTime.astimezone(UK).date()
"""

class Event:
    """
    attribute | type
    start_date | datetime.date
    start_time | datetime.time
    duration | int (minutes) 
    """

    id_counter = itertools.count()

    def __init__(
        self,
        name,
        id=None,
        description=None,
        start_date=None,
        start_time=None,
        duration=None,
        tag=None,
        location=None
    ):
        self.name = name
        self.id = next(Event.id_counter)
        self.description = description
        self.start_date = start_date
        self.start_time = start_time
        self.duration = duration
        self.tag = tag
        self.location = location

    def __str__(
    self
    ):
        return f"{getattr(self, 'name', None)}, {getattr(self, 'id', None)}, {getattr(self, 'description', None)}, {getattr(self, 'start_date', None)}, {getattr(self, 'start_time', None)}, {getattr(self, 'duration', None)}, {getattr(self, 'tag', None)}, {getattr(self, 'location', None)}"
    # change name
    def SetName(
        self, 
        new_name
    ):
        self.name = new_name
    
    # change description
    def SetDesc(
        self,
        new_desc
    ):
        self.description = new_desc

    # set start date (calendar events need dates to be added)
    def SetDate(
        self,
        new_start_date
    ):
        self.start_date = new_start_date

    # set start time (this should be optional)
    def SetTime(
        self,
        new_start_time
    ):
        self.start_time = new_start_time

    # set duration (this should be optional)
    def SetDuration(
        self,
        new_duration
    ):
        self.duration = new_duration

    # set tag
    def SetTag(
        self,
        new_tag
    ):
        self.tag = new_tag

    def setLocation(
            self,
            new_location
    ):
        self.location = new_location

class Display:
    def __init__(
        self
    ):
        pass

# make a plan for continuing this later
