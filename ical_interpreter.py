import json
import requests
from icalendar import Calendar
from datetime import datetime
from zoneinfo import ZoneInfo
from cal import Event

UK = ZoneInfo("Europe/London")

#Takes the name to a calendar and its link and saves it to a json file on local disk.

def save_tabula_calendar(
        name, link
    ):

    data = {
        "name": name,
        "tabulaCalendarLink": link
    }

    # WARNING we might need to use pathlib to REALLY make sure this file is always in the right place.
    with open ("calendarLink.json", "w") as f:
        json.dump(data, f)

#Similarly as above

def save_moodle_calendar(
        name, link
    ):

    data = {
        "name": name,
        "moodleCalendarLink": link
    }

    # Same warning as above
    with open ("calendarLink.json", "w") as f:
        json.dump(data, f)


def get_tabula_calendar(link):
    """
    Takes a tabula calendar link and returns a list of Events.
    """

    calendar = []

    raw = requests.get(link).content
    cal = Calendar.from_ical(raw)
    events = cal.walk("VEVENT")
    for event in events:
        
        name = str(event.get("SUMMARY"))
        description = str(event.get("DESCRIPTION", "")) # literally have one thing on the calendar with a description for some reason
        location = str(event.get("LOCATION"))
        dateTimeStart = event.get("DTSTART").dt
        dateTimeEnd = event.get("DTEND").dt
        start_date = dateTimeStart.astimezone(UK).date()
        start_time = dateTimeStart.astimezone(UK).time()
        duration = ((dateTimeEnd - dateTimeStart).total_seconds()) // 60 # Stored in minutes

        print([name, description, location, start_date])

        calendar.append(Event(name=name, description=description, location=location, start_date=start_date, start_time=start_time, duration=duration))
    
    return calendar




print(get_tabula_calendar(r"https://tabula.warwick.ac.uk/api/v1/timetable/calendar/e2a54357-c95a-4f55-9df6-95d0b9e6cbbf.ics")[1])



