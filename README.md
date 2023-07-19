# Task Manager

The Task Manager is a Python-based application that helps users manage and track tasks. It provides features for user registration, login, adding tasks, viewing tasks, generating reports, and more.

## Features

- User Registration: Users can register with unique usernames and passwords.
- User Login: Registered users can log in to access the task manager functionalities.
- Add Task: Users can add new tasks with details such as title, description, assignee, and due date.
- View All Tasks: Users can view all tasks in the system.
- View My Tasks: Users can view tasks assigned to them.
- Generate Reports: Admin users can generate reports to analyze task statistics.
- Statistics: Admin users can view statistics related to task completion and user tasks.

## Getting Started

To run the Task Manager on your local machine, follow these steps:

1. Clone the repository: `git clone https://github.com/your-username/task-manager.git`
2. Navigate to the project directory: `cd task-manager`
3. Install the required dependencies: `pip install -r requirements.txt`
4. Run the application: `python main.py`

Make sure you have Python 3.x and pip installed on your system.

## Project Structure

- `main.py`: The main entry point of the application.
- `task_manager.py`: Contains the `TaskManager` class and its methods.
- `user.txt`: Text file for storing user registration details.
- `tasks.txt`: Text file for storing task information.
- `task_overview.txt`: Generated report file for task overview.
- `user_overview.txt`: Generated report file for user overview.

## Contributing

Contributions to the Task Manager project are welcome! If you find any bugs, have suggestions for improvements, or would like to add new features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.
