
def task_reminder(time_as_string):

    if time_as_string == "7:00 a.m.":
        task = "Set up a to-do list"
    elif time_as_string == "9:00 a.m.":
        task = "Reply to emails and align calendar"
    elif time_as_string == "12:00 p.m.":
        task = "Go for a lunch break"
    elif time_as_string == "2:00 p.m.":
        task = "Prepare report for manager"
    elif time_as_string == "4:00 p.m.":
        task = "Done for the day"
    else:
        task = "Nothing assigned"

    return task

print(task_reminder("2:00 p.m.")) 