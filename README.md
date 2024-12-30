# Task Management System

A powerful and intuitive **Task Management System** built using **Python**, **Tkinter**, and **SQL** for organizing and tracking tasks efficiently. This system is designed to help users manage their to-do lists, track progress, and enhance productivity.

---

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
  - [Installation](#installation)
  - [Database Setup](#database-setup)
  - [Usage](#usage)
- [Screenshots](#screenshots)
- [Project Structure](#project-structure)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Features

- **Add, Edit, and Delete Tasks**: Manage your tasks with a user-friendly interface.
- **Categorize Tasks**: Group tasks by priority or category.
- **Track Task Progress**: Mark tasks as complete or in-progress.
- **Search Functionality**: Quickly find tasks using keywords.
- **SQL Database Integration**: All data is stored securely in an SQL database.
- **Responsive Interface**: Built with Tkinter for a clean and interactive UI.

---

## Technologies Used

- **Programming Language**: Python
- **GUI Library**: Tkinter
- **Database**: SQLite
- **IDE**: VSCode (or any Python-supported IDE)

---

## Getting Started

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/YourUsername/Task-Management-System.git
   cd Task-Management-System
   ```

2. Install the required Python libraries:

   ```bash
   pip install -r requirements.txt
   ```

### Database Setup

- The project uses SQLite for storing task data.
- Ensure the `tasks.db` file is in the root directory.
- If not, run the provided SQL script `initialize_db.sql` to create the database schema:
  ```bash
  sqlite3 tasks.db < initialize_db.sql
  ```

### Usage

1. Run the application:
   ```bash
   python main.py
   ```
2. Use the interface to add, update, or delete tasks.
3. Data is automatically saved in the SQLite database.

---

## Screenshots

### Dashboard



### Add Task Window



*(Replace placeholder images with actual screenshots from your project.)*

---

## Project Structure

```
Task-Management-System/
|— main.py            # Entry point of the application
|— database.py        # Handles database connections and queries
|— gui.py             # Contains Tkinter GUI logic
|— tasks.db          # SQLite database file
|— initialize_db.sql  # SQL script to initialize the database
|— README.md          # Project documentation
|— requirements.txt   # Dependencies
```

---

## Future Enhancements

- Add a **Calendar View** for tasks.
- Implement **User Authentication** for multi-user support.
- Enable **Export to CSV** feature for task data.
- Add **Notifications** and reminders for pending tasks.

---

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature name"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a Pull Request.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

## Contact

- **Developer**: santhoshmahendran
- **Email**: santhoshm2000411\@email.com
- **GitHub Repository**: [Task Management System](https://github.com/YourUsername/Task-Management-System)

---

