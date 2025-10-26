# 🧠 Study Planner

A **Python + MySQL based Study Planner** that helps students organize their study schedules, track tasks, and manage deadlines efficiently.  
This project was created as part of the **CBSE Class XII Computer Science Project** (Subject Code: 083).

---

## 📘 Overview

The **Study Planner** is a simple yet effective task management system designed specifically for students.  
It allows users to:
- Add and manage study tasks.
- Set priorities (High, Medium, Low).
- View, edit, and delete tasks.
- Mark tasks as completed.
- Generate progress reports.

This project integrates **Python** (for logic and user interface) with **MySQL** (for data storage and management).

---

## 🧩 Features

✅ **User Registration & Login**  
Each user can create an account and log in securely.

✅ **Task Management**  
Add, view, update, or delete study tasks with ease.

✅ **Task Prioritization**  
Set task importance levels (High, Medium, or Low).

✅ **Progress Report**  
Displays total, completed, and pending tasks for motivation.

✅ **Database Integration**  
All data is stored and managed through a MySQL database.

---

## ⚙️ Tech Stack

- **Programming Language:** Python  
- **Database:** MySQL  
- **Library Used:** `mysql.connector`  

---

## 🛠️ Installation & Setup

1. **Install Python**  
   Download and install Python 3.8 or higher from [python.org](https://www.python.org/downloads/).

2. **Install MySQL**  
   Install MySQL Community Server and MySQL Workbench from [mysql.com](https://dev.mysql.com/downloads/).

3. **Install MySQL Connector for Python**  
   Open your terminal or command prompt and run:
   ```bash
   pip install mysql-connector-python

4.Create Database and Tables
CREATE DATABASE studyplanner;

USE studyplanner;

CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100),
    password VARCHAR(100)
);

CREATE TABLE tasks (
    task_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    task_name VARCHAR(255),
    subject VARCHAR(100),
    priority VARCHAR(20),
    deadline DATE,
    status VARCHAR(20) DEFAULT 'Pending',
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

5.Run the Program
Save your Python file (e.g., study_planner.py) and run it using:
python study_planner.py

🧮 Functionality Summary
| Function            | Description                                                      |
| ------------------- | ---------------------------------------------------------------- |
| `add_task()`        | Add a new task with details like subject, deadline, and priority |
| `view_tasks()`      | Display all tasks for the logged-in user                         |
| `mark_completed()`  | Update task status to “Completed”                                |
| `edit_task()`       | Edit existing task details                                       |
| `delete_task()`     | Remove a task permanently                                        |
| `progress_report()` | Show total, completed, and pending tasks                         |

📂 Folder Structure
StudyPlanner/
│
├── study_planner.py      # Main source code
├── README.md             # Project documentation
└── requirements.txt      # Dependencies (optional)

