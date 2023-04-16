import datetime
import time

calendar = {}

def add_event():
    event = input("Enter the event: ")
    date = input("Enter the date (in the format dd-mm-yyyy): ")
    time = input("Enter the time (in the format hh:mm): ")
    datetime_str = date + ' ' + time
    datetime_obj = datetime.datetime.strptime(datetime_str, '%d-%m-%Y %H:%M')
    calendar[datetime_obj] = {'event': event, 'done': False}
    print("Event added to calendar.")

def mark_as_done():
    for event_time in calendar:
        if not calendar[event_time]['done']:
            print(f"{calendar[event_time]['event']} at {event_time.strftime('%d-%m-%Y %H:%M')} - (Enter 'Y' if done, any other key to skip)")
            done = input().strip().lower()
            if done == 'y':
                calendar[event_time]['done'] = True

def check_reminder():
    current_time = datetime.datetime.now()
    for event_time in calendar:
        if not calendar[event_time]['done'] and current_time >= event_time:
            print(f"Reminder: {calendar[event_time]['event']} at {event_time.strftime('%d-%m-%Y %H:%M')}")

if __name__ == '__main__':
    while True:
        print("Type the numer of the command you want to execute!")
        print("1. Add event")
        print("2. Mark as done")
        print("3. Check reminder")
        print("4. Quit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_event()
        elif choice == '2':
            mark_as_done()
        elif choice == '3':
            check_reminder()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Try again.")
