# Library

from datetime import datetime

# Features for the output menus and messages

PINK = '\033[95m'
BLUE = '\033[94m'
CYAN = '\033[96m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
WHITE = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

# Global variable

user_dict = {}

# Defining functions

def reg_user():

    new_user = input(f"{BOLD}{RED}New username:{WHITE} ")
    while new_user in user_dict:
        print(f"{BOLD}{RED}Invalid username! The user is already registered.{WHITE}")
        new_user = input("New username: ")

    user_dict[new_user] = get_password(new_user)

    user_file = open("user.txt", 'a')
    user_file.write(f"\n{new_user}, {user_dict[new_user]}")
    user_file.close()


def get_password(username):  # Calling this function with the name of the user for the displaying messages

    new_password = input(f"Password for {username}: ")
    confirm_psw = input("Confirm password: ")

    while new_password != confirm_psw:
        print(f"{BOLD}{RED}Passwords don't match!{WHITE}")
        new_password = input(f"Password for {username}: ")
        confirm_psw = input("Confirm password: ")

    return new_password


def add_task():

    task_user = input("Username the new task will be assigned to: ")
    task_title = input("New task title (don't use comas please): ")
    task_description = input("Task description (don't use comas please): ")

    # Adding a validation feature for date format following guidance from Thabiso Mathebula in complementary lectures

    while True:
        try:
            task_due = input("New task should be completed by (DD MMM YYYY): ")
            datetime.strptime(task_due, '%d %b %Y')
            break
        except:
            print(f"Invalid date. Please use this format (DD MMM YYYY), example {datetime.today().strftime('%d %b %Y')} ")

    task_dated = datetime.today().strftime('%d %b %Y')

    tasks_file = open("tasks.txt", 'a')
    tasks_file.write(f"\n{task_user}, {task_title}, {task_description}, {task_dated}, {task_due}, No")
    tasks_file.close()


def read_tasks():   # I'm calling this function in four other functions view_all(), view_mine() and gen_reports()

    tasks_read = open('tasks.txt', 'r')
    data = tasks_read.readlines()
    tasks_read.close()

    return data


def view_all():

    data = read_tasks()

    for i, line in enumerate(data):

        split_data = line.strip('\n').split(", ")
        print_task_header(BLUE)
        print_task(i + 1, split_data, BLUE)
        print_task_footer(BLUE)

# Simplifying output messages with printing options to add headers and footers

def print_task_header(COLOUR):

    print(f'\n{BOLD}{COLOUR}─────────────────────────────────────────{WHITE}\n')


def print_task_footer(COLOUR):

    print(f'{BOLD}{COLOUR}─────────────────────────────────────────{WHITE}')


# Displaying all tasks in a manner that is easy to read and each task is displayed with a corresponding number.
# I've called this function in view_all() and view_mine(), using different colours with COLOUR as an argument

def print_task(n, split_data, COLOUR):

    print(f'{UNDERLINE}{COLOUR}Task number {n}:{WHITE} \t\t{split_data[1]}')
    print(f'{UNDERLINE}{COLOUR}Assigned to:{WHITE} \t\t{split_data[0]}')
    print(f'{UNDERLINE}{COLOUR}Date assigned:{WHITE} \t\t{split_data[3]}')
    print(f'{UNDERLINE}{COLOUR}Due date:{WHITE} \t\t\t{split_data[4]}')
    print(f'{UNDERLINE}{COLOUR}Task complete?{WHITE} \t\t{split_data[5]}')
    print(f'{UNDERLINE}{COLOUR}Task description:{WHITE} \t{split_data[2]}\n')


def view_mine(user):

    # I'm using two dictionaries to organise and edit data in this function my_tasks and tasks_dict

    i = 0
    my_tasks = {}

    data = read_tasks()

    for line in data:

        split_data = line.strip('\n').split(", ")

        if user == split_data[0]:

            i += 1
            print_task_header(YELLOW)
            print_task(i, split_data, YELLOW)

            my_tasks[i] = split_data

        else:

            continue

    print_task_footer(YELLOW)

    tasks_dict = {}

    if i == 0:

        print("No tasks assigned to you.\n")

    else:

        while True:

            task_index = int(input("\nEnter task number for further options or -1 to return to main menu: "))

            if task_index == -1:

                return

            elif task_index <= 0 or task_index > i:

                print("Invalid task number. Try again please!")
                continue

            else:

                print(f"\nTask {task_index}: {my_tasks[task_index][1]}")

                while True:

                    action = input(f"\nMark the task as ({BOLD}{UNDERLINE}C{WHITE})omplete "
                               f"or ({BOLD}{UNDERLINE}E{WHITE})dit task? ").upper()

                    # Making sure user's input is valid within the options given for action C or E

                    if action == 'C' or action == 'E':

                        break

                    else:

                        print(f"\nWrong choice. Please type {BOLD}{UNDERLINE}C{WHITE} or {BOLD}{UNDERLINE}E{WHITE}")
                        continue

                if my_tasks[task_index][5].lower() == 'no':

                    if action == 'C':

                        my_tasks[task_index][5] = 'Yes'

                    elif action == 'E':

                        while True:

                            choice = input(f"\nEdit ({BOLD}{UNDERLINE}U{WHITE})sername "
                                       f"or ({BOLD}{UNDERLINE}D{WHITE})ue date? ").upper()

                            # Making sure user's input is valid within the options given for choice U or D

                            if choice == 'U' or choice == 'D':

                                break

                            else:

                                print(
                                    f"\nWrong choice. Please type {BOLD}{UNDERLINE}U{WHITE} or {BOLD}{UNDERLINE}D{WHITE}")
                                continue

                        if choice == 'U':

                            my_tasks[task_index][0] = input("New username: ")

                        elif choice == 'D':

                            while True:

                                # Checking the date input fits the format suggested

                                try:
                                    task_due = input("\nThis task should be completed by (DD MMM YYYY): ")
                                    datetime.strptime(task_due, '%d %b %Y')
                                    my_tasks[task_index][4] = task_due
                                    break
                                except:
                                    print(f"Invalid date. Please use this format (DD MMM YYYY), example {datetime.today().strftime('%d %b %Y')} ")

                else:

                    print("The task has been completed. You can't make changes now")

                # I'll use two counters next to move through both dictionaries following the structure of the tasks.txt file

                n = 0
                ut = 1

                for line in data:

                    split_data = line.strip('\n').split(", ")

                    if user == split_data[0]:

                        tasks_dict[n] = my_tasks[ut]
                        ut +=1

                    else:

                        tasks_dict[n] = split_data

                    n += 1

            all_tasks = [', '.join(t) for t in tasks_dict.values()]

            # Updating the file tasks.txt with the edited version

            with open("tasks.txt", 'w') as tk_file:
                tk_file.write('\n'.join(all_tasks))


def gen_reports():

    data = read_tasks()

    tasks_dict = {}  # I'll be using a dictionary of counters to collect data from different users' tasks

    incomplete = 0
    overdue = 0
    complete = 0

    # This 1st for loop is to count the total incomplete and overdue tasks for task_overview.txt

    for line in data:

        split_data = line.strip('\n').split(", ")

        if split_data[5].lower() == 'no':

            incomplete += 1
            due_date = split_data[-2]
            date_objc = datetime.strptime(due_date, '%d %b %Y')
            curr_date = datetime.today()

            if date_objc < curr_date:

                overdue += 1

        else:

            complete += 1

    # This 2nd for loop is to count the total tasks per user for user_overview.txt

    for x in user_dict:

        tasks_dict[x] = [0, 0, 0]

        for line in data:

            split_data = line.strip('\n').split(", ")

            if x == split_data[0]:

                tasks_dict[x][0] += 1

    # This 3rd for loop is to count the total of incomplete and overdue tasks per user for user_overview.txt

    for key in tasks_dict.keys():

        for line in data:

            split_data = line.strip('\n').split(", ")

            if split_data[0] == key:

                if split_data[5].lower() == 'no':

                    tasks_dict[key][1] += 1  # This is the counter for incomplete tasks per user
                    due_date = split_data[-2]
                    date_objc = datetime.strptime(due_date, '%d %b %Y')
                    curr_date = datetime.today()

                    if date_objc < curr_date:

                        tasks_dict[key][2] += 1   # # This is the counter for incomplete and overdue tasks per user


    total_tasks = len(data)
    total_users = len(user_dict.keys())
    per_incom = round((incomplete / total_tasks) * 100, 2)
    per_overd = round((overdue / total_tasks) * 100, 2)

    # Generating text file task_overview.txt for report

    with open("task_overview.txt", 'w') as tsk_ov:

        tsk_ov.write(f"{total_tasks}, {complete}, {incomplete}, {overdue}, {per_incom}, {per_overd}")

    # Generating text file user_overview.txt for report

    with open("user_overview.txt", 'w') as usr_ov:

        usr_ov.write(f"{total_users}, {total_tasks}\n")

    with open("user_overview.txt", 'a') as usr_ov:

        for x, y in tasks_dict.items():  # Moving through the dictionary to calculate the stats and add them to user_overview.txt

            if y[0] != 0:

                perc_of_total = round(y[0] / total_tasks * 100, 2)
                user_incompl_rate = round(y[1] / y[0] * 100, 2)
                user_compl_rate = round(100 - user_incompl_rate, 2)
                user_inc_ovd_rate = round(y[2] / y[0] * 100, 2)

                usr_ov.write(f"{x}, {y[0]}, {perc_of_total}, {user_compl_rate}, {user_incompl_rate}, {user_inc_ovd_rate}\n")

            else:

                usr_ov.write(f"{x}, none\n")


def dpl_stats():

    gen_reports()  # Calling the code to generate the text files

    with open("task_overview.txt", 'r') as tsk_ov:

        data = tsk_ov.readline()

        split_data = data.strip('\n').split(", ")

    print_task_header(GREEN)

    # Printing the first report from task_overview.txt in an easy to read manner

    print(f"{UNDERLINE}{GREEN}Total of tasks generated and tracked:{WHITE} \t{split_data[0]}"
          f"\n{UNDERLINE}{GREEN}Completed tasks:{WHITE} \t\t\t\t\t\t{split_data[1]}"
          f"\n{UNDERLINE}{GREEN}Incompleted tasks:{WHITE} \t\t\t\t\t\t{split_data[2]}"
          f"\n{UNDERLINE}{GREEN}Incompleted & overdue tasks:{WHITE} \t\t\t{split_data[3]}"
          f"\n{UNDERLINE}{GREEN}Percentage of incomplete tasks:{WHITE} \t\t{split_data[4]}%"
          f"\n{UNDERLINE}{GREEN}Percentage of overdue tasks:{WHITE} \t\t\t{split_data[5]}%\n")

    print_task_header(GREEN)

    with open("user_overview.txt", 'r') as usr_ov:

        data = usr_ov.readlines()

        i = 0

        for line in data:

            split_data = line.strip('\n').split(", ")

            if i == 0:

                # Printing the second report from user_overview.txt in an easy to read manner

                print(f"{UNDERLINE}{GREEN}Total of users registered:{WHITE} \t\t\t\t{split_data[0]}"
                      f"\n{UNDERLINE}{GREEN}Total of tasks generated and tracked:{WHITE} \t{split_data[1]}\n")
                i += 1

            else:

                if split_data[1] != 'none':

                    print(f"{BOLD}{UNDERLINE}{GREEN}{split_data[0]}{WHITE}:  "
                          f"\tTasks = {BOLD}{UNDERLINE}{GREEN}{split_data[1]}{WHITE}, "
                          f"{BOLD}{UNDERLINE}{GREEN}{split_data[2]}%{WHITE} of total; "
                          f"of which {BOLD}{UNDERLINE}{GREEN}{split_data[3]}%{WHITE} completed, "
                          f"{BOLD}{UNDERLINE}{GREEN}{split_data[4]}%{WHITE} incompleted "
                          f"and {BOLD}{UNDERLINE}{GREEN}{split_data[5]}%{WHITE} overdue ")

                else:

                    print(f"{BOLD}{UNDERLINE}{GREEN}{split_data[0]}{WHITE}: \t{BOLD}{UNDERLINE}No tasks assigned yet{WHITE}")

    print_task_header(GREEN)



### * Main ###

# Populating user_dict by extracting usernames and passwords from user.txt

with open("user.txt", 'r') as user_file:

    for line in user_file:
        user, psw = line.strip("\n").split(", ")
        user_dict[user] = psw

# Validating login access

while True:

    username = input("Username: ")
    error_msg = f"{BOLD}{RED}Invalid username!{WHITE}"
    resp = user_dict.get(username, error_msg)
    if resp != error_msg:

        password = input("Password: ")
        if password == user_dict[username]:
            break
        else:
            print(f"{BOLD}{RED}Invalid password!{WHITE}")
    else:
        print(resp)


# Displaying menus and calling functions

while True:

    print(f"\n{BOLD}{GREEN}Welcome to the tasks manager!{WHITE}")

    if username == 'admin':

        menu = input(f"Please select one of the following options below:"
                     f"\n\t{BOLD}{PINK}a{WHITE} - Adding a task"
                     f"\n\t{BOLD}{BLUE}va{WHITE} - View all tasks"
                     f"\n\t{BOLD}{YELLOW}vm{WHITE} - View my task(s)"
                     f"\nAdmin only options:"
                     f"\n\t{BOLD}{RED}r{WHITE} - Registering a user"
                     f"\n\t{BOLD}{CYAN}gr{WHITE} - Generate reports"
                     f"\n\t{BOLD}{GREEN}st{WHITE} - View stats"
                     f"\ne - Exit: ").lower()

    else:

        menu = input(f"Please select one of the following options below:"
                     f"\n\t{BOLD}{PINK}a{WHITE} - Adding a task"
                     f"\n\t{BOLD}{BLUE}va{WHITE} - View all tasks"
                     f"\n\t{BOLD}{YELLOW}vm{WHITE} - View my task(s)"
                     f"\n\te - Exit: ").lower()

    if menu == 'r' or menu == 'st' or menu == 'gr':

        if username == 'admin':

            if menu == 'r':

                reg_user()

            elif menu == 'st':

                dpl_stats()

            elif menu == 'gr':

                gen_reports()

        else:

            print(f"{BOLD}{RED}Invalid username!{WHITE}"
                  f"\nOnly admin can access this option")
            continue

    elif menu == 'a':

        add_task()

    elif menu == 'va':

        view_all()

    elif menu == 'vm':

        view_mine(username)

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("\nWrong choice!\nPlease Try again\n")
