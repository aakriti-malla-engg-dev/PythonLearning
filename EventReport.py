# Problem Statement : Input a list of event objects and evaluate these objects attributes to output a report of all the
# users currently logged into a machine.


def get_event_date(event):
    return event.date


def current_users(events):
    events.sort(key=get_event_date)
    machines = {}
    for event in events:
        if event.machine not in machines:
            machines[event.machine] = set()
        if event.type == 'login':
            machines[event.machine].add(event.user)
        elif event.type == 'logout':
            machines[event.machine].remove(event.user)
    return machines


def generate_report(machines):
    for machine, users in machines.items():
        if len(users) > 0:
            user_list = ", ".join(users)
            print(f"{machine} : {users}")


class Event:
    def __init__(self, event_date, machine_name, user, event_type):
        self.date = event_date
        self.machine = machine_name
        self.user = user
        self.type = event_type


events = [
    Event('2-2-2023 12:02:02', 'data', 'pia', 'login'),
    Event('2-2-2023 13:02:05', 'data', 'pia', 'logout'),
    Event('2-2-2023 11:02:05', 'work', 'abc', 'login'),
    Event('2-2-2023 10:02:05', 'beast', 'sia', 'login'),
    Event('2-2-2023 07:02:05', 'work', 'kia', 'login'),
]

users = current_users(events)
print(users)

generate_report(users)
