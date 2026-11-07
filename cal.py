import itertools

class Event:

    id_counter = itertools.count()

    def __init__(
        self,
        name,
        id=None,
        description=None,
        start_date=None,
        start_time=None,
        duration=None,
        tag=None
    ):
        self.name = name
        self.id = next(Event.id_counter)

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

class Display:
    def __init__(
        self
    ):
        pass
