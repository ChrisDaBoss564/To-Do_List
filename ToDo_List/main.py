print("Hello World!")

ToDo = {
    "Monday": [],
    "Tuesday": [],
    "Wednesday": [],
    "Thursday": [],
    "Friday": [],
    "Saturday": [],
    "Sunday": []
}

def add_task(day, task):
    ToDo[day].append(task);

def remove_task(day, task):
    ToDo[day].remove(task);

def get_tasks(day):
    return ToDo[day];

def get_all_tasks():
    return ToDo;

