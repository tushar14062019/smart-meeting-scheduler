# Application

import datetime

class Sport_Meeting_Schedular:
    def __init__(self, working_time=(9, 17), holidays=None):
        self.working_time = working_time
        self.holidays = holidays if holidays else []
        self.schedule = {}  
    def WOrking_Day(self, date):
        if date.weekday() >= 5 or date in self.holidays:
            return False
        return True

    def initialize_user(self, user):
        if user not in self.schedule:
            self.schedule[user] = []

    def schedule_meeting(self, user, date, start_time, end_time):
        self.initialize_user(user)

        if not self.WOrking_Day(date):
            print("Error: Cannot schedule meetings on holidays.")
            return

        new_meeting = (start_time, end_time)
        for meeting in self.schedule[user]:
            if max(meeting[0], new_meeting[0]) < min(meeting[1], new_meeting[1]):
                print("Error: Overlapping meeting.")
                return

        self.schedule[user].append(new_meeting)
        print("Meeting scheduled successfully.")

    def Slots_Available(self, user, date):
        self.initialize_user(user)

        if not self.WOrking_Day(date):
            print("There are no available slots. It's a holiday.")
            return

        booked_slots = sorted(self.schedule[user])
        available_slots = []

        current_time = self.working_time[0]
        for meeting in booked_slots:
            if current_time < meeting[0]:
                available_slots.append((current_time, meeting[0]))
            current_time = max(current_time, meeting[1])

        if current_time < self.working_time[1]:
            available_slots.append((current_time, self.working_time[1]))

        if available_slots:
            print("Available slots:")
            for slot in available_slots:
                print(f"{slot[0]}:00 - {slot[1]}:00")
        else:
            print("There are no available slots.")

    def view_meetings(self, user):
        self.initialize_user(user)

        if self.schedule[user]:
            print(f"Show Upcoming meetings {user}:")
            for meeting in sorted(self.schedule[user]):
                print(f"{meeting[0]}:00 - {meeting[1]}:00")
        else:
            print("There are no meetings.")

scheduler = Sport_Meeting_Schedular(holidays=[datetime.date(2025, 3, 21)])
user = "Anuj"
date = datetime.date(2025, 2, 25)

scheduler.Slots_Available(user, date)

scheduler.schedule_meeting(user, date, 12, 13)

scheduler.view_meetings(user)
