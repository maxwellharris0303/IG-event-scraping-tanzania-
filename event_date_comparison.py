from datetime import datetime

def comparison_event_date(event_date_str, year, month, day):
    # Event details
    # event_date_str = "2024-04-09"
    event_date = datetime.strptime(event_date_str, "%Y-%m-%d")


    # Compare with August 1
    comparison_date = datetime(year, month, day)

    # Check if the event date is after August 1
    if event_date > comparison_date:
        return True
    else:
        return False
