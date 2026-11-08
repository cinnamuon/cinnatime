import json

#Takes the name to a calendar and its link and saves it to a json file on local disk.
def save_calendar(
        name, link
    ):

    data = {
        "name": name,
        "calendarLink": link
    }

    with open ("calendarLink.json", "w") as f:
        json.dump(data, f)


