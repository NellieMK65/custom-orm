# O.O.P

"""
    Principles
    - Inheritance
    - Abstraction
    - Polymorphism
    - Encapsulation

    Attributes (Properties) -> Class & Instance
    - Venue
    - members
    - Host
    - Time

    Methods (Behaviour)
    - Record
    - Share Screen
"""

# Instance of a class -> object
# class Meeting:
#     # class attribute
#     school = "Moringa School"

#     # the init method is autamitcally called every time a new instance of the class is made
#     def __init__(self, venue, members, host, time):
#         self.venue = venue
#         self.members = members
#         self.host = host
#         self.time = time

#     # instance method
#     def start_recording(self):
#         print(f"{self.host} has started recoring the meeting")
#         self.stop_recording()

#     def stop_recording(self):
#         print(f"{self.host} has stopped recording")

#     # use this decorator to define class method
#     @classmethod
#     def print_school_name(cls):
#         print(f"{cls.school}")

# python_catchup = Meeting("Remote", ['Joel', 'Dennis'], "Nelson", "2-3pm")

# print(python_catchup.members)
# python_catchup.start_recording()

# morning_standup = Meeting("Room 302", ['George'], 'Andrew', "9-10AM")

# print(morning_standup.members)
# Meeting.print_school_name()
# morning_standup.start_recording()


# Start of app logic
from models.meeting import Meeting


def app():
    while True:
        print(f"Welcome meeting management app")

        print("1. Create meeting")
        print("2. Update meeting")
        print("3. Get single meeting")
        print("4. Get all meetings")

        choice = input("Enter your choice to continue: ")

        if choice == "1":
            print("=======Creating meeting======== \n")
            host = input("Enter meeting host: ")
            members = input("Enter meeting members: ")
            time = input("Enter meeting time: ")
            venue = input("Enter the venue: ")

            meeting = Meeting(venue, members, host, time)
            meeting.save()

        elif choice == "3":
            print("======Getting a single meeting====== \n")
            meeting_id = input("Enter meeting id: ")

            meeting = Meeting.find_one(meeting_id)

            print(meeting)


app()
