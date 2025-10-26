import mysql.connector
from datetime import datetime

# Connecting to MySQL
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Rabeeh",
        database="study_planner"
    )

# Creating a new user
def create_user():
    conn = connect_db()
    cursor = conn.cursor()
    
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    query = "INSERT INTO users (username, password) VALUES (%s, %s)"
    cursor.execute(query, (username, password))
    conn.commit()
    
    print("User created successfully!")
    
    cursor.close()
    conn.close()

# Login user
def login():
    conn = connect_db()
    cursor = conn.cursor()
    
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    query = "SELECT user_id FROM users WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))
    user = cursor.fetchone() #cursor.fetchone returns a tuple with corresponding user as first element
    
    if user:
        print("Login successful!")
        return user[0]
    else:
        print("Login failed!")
        return None

# Adding a new task
def add_task(user_id):
    conn = connect_db()
    cursor = conn.cursor()
    
    task_name = input("Enter task name: ")
    subject = input("Enter subject: ")
    deadline = input("Enter deadline (YYYY-MM-DD): ")
    
    # Validating priority input (incase of a spelling error)
    valid_priorities = ['High', 'Medium', 'Low']
    priority = input("Enter priority (High, Medium, Low): ")
    
    while priority not in valid_priorities:
        print(f"Invalid priority. Please enter one of the following: {', '.join(valid_priorities)}")
        priority = input("Enter priority (High, Medium, Low): ")
        
    query = "INSERT INTO tasks (task_name, subject, deadline, priority, user_id) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, (task_name, subject, deadline, priority, user_id))
    conn.commit()
    
    print("Task added successfully!")
    
    cursor.close()
    conn.close()

# Viewing tasks
def view_tasks(user_id):
    conn = connect_db()
    cursor = conn.cursor()
    
    query = "SELECT task_id, task_name, subject, deadline, priority, status FROM tasks WHERE user_id = %s"
    cursor.execute(query, (user_id,))
    tasks = cursor.fetchall()
    
    if tasks:
        print("\nYour Tasks:")
        for task in tasks:
            print(f"ID: {task[0]}, Task: {task[1]}, Subject: {task[2]}, Deadline: {task[3]}, Priority: {task[4]}, Status: {task[5]}")
    else:
        print("No tasks found.")
        
    cursor.close()
    conn.close()

# Marking a task as completed
def mark_completed(user_id):
    conn = connect_db()
    cursor = conn.cursor()
    
    # Fetch tasks for the logged-in user and display them (as the user might not know the task id)
    query = "SELECT task_id, task_name, subject, deadline, priority, status FROM tasks WHERE user_id = %s"
    cursor.execute(query, (user_id,))
    tasks = cursor.fetchall()
    
    if tasks:
        print("\nYour Tasks:")
        for task in tasks:
            print(f"ID: {task[0]}, Task: {task[1]}, Subject: {task[2]}, Deadline: {task[3]}, Priority: {task[4]}, Status: {task[5]}")
    else:
        print("No tasks found.")
        cursor.close()
        conn.close()
        return
        
    # Prompt user for the Task ID to mark as completed
    task_id = input("Enter the Task ID to mark as completed: ")
    
    # Check if the task ID exists in the database
    query = "SELECT * FROM tasks WHERE task_id = %s AND user_id = %s"
    cursor.execute(query, (task_id, user_id))
    task = cursor.fetchone()
    
    if task:
        query = "UPDATE tasks SET status = 'Completed' WHERE task_id = %s AND user_id = %s"
        cursor.execute(query, (task_id, user_id))
        conn.commit()
        print("Task marked as completed!")
    else:
        print("Invalid Task ID. Please enter a valid Task ID from your task list.")
        
    cursor.close()
    conn.close()

# Show pending tasks with reminders
def show_reminders(user_id):
    conn = connect_db()
    cursor = conn.cursor()
    
    query = "SELECT task_name, deadline, priority FROM tasks WHERE user_id = %s AND status = 'Pending' AND deadline >= CURDATE()"
    cursor.execute(query, (user_id,))
    tasks = cursor.fetchall()
    
    if tasks:
        print("\nUpcoming Tasks:")
        for task in tasks:
            print(f"Task: {task[0]}, Deadline: {task[1]}, Priority: {task[2]}")
    else:
        print("No upcoming tasks.")
        
    cursor.close()
    conn.close()

# Deleting a task
def delete_task(user_id):
    conn = connect_db()
    cursor = conn.cursor()
    
    # Fetch tasks for the logged-in user and display them
    query = "SELECT task_id, task_name, priority, status FROM tasks WHERE user_id = %s"
    cursor.execute(query, (user_id,))
    tasks = cursor.fetchall()
    
    if tasks:
        print("\nYour Tasks:")
        for task in tasks:
            print(f"ID: {task[0]}, Task: {task[1]}, Priority: {task[2]}, Status: {task[3]}")
    else:
        print("No tasks found.")
        cursor.close()
        conn.close()
        return
        
    # Prompt user for the Task ID to delete
    task_id = input("Enter the Task ID to delete: ")
    query = "DELETE FROM tasks WHERE task_id = %s AND user_id = %s"
    cursor.execute(query, (task_id, user_id))
    conn.commit()
    
    if cursor.rowcount > 0:
        print("Task deleted successfully!")
    else:
        print("Task ID not found or does not belong to you.")
        
    cursor.close()
    conn.close()

# Edit a task
def edit_task(user_id):
    conn = connect_db()
    cursor = conn.cursor()
    
    # Fetch tasks for the logged-in user and display them
    query = "SELECT task_id, task_name, subject, deadline, priority, status FROM tasks WHERE user_id = %s"
    cursor.execute(query, (user_id,))
    tasks = cursor.fetchall()
    
    if tasks:
        print("\nYour Tasks:")
        for task in tasks:
            print(f"ID: {task[0]}, Task: {task[1]}, Subject: {task[2]}, Deadline: {task[3]}, Priority: {task[4]}, Status: {task[5]}")
    else:
        print("No tasks found.")
        cursor.close()
        conn.close()
        return
        
    # Prompt user for the Task ID to edit
    task_id = input("Enter the Task ID to edit: ")
    
    # Fetching the current details of the task to show to the user
    query = "SELECT * FROM tasks WHERE task_id = %s AND user_id = %s"
    cursor.execute(query, (task_id, user_id))
    task = cursor.fetchone()
    
    # Displaying current task details
    if task:
        print(f"Current Task Details: ID: {task[0]}, Task: {task[1]}, Subject: {task[2]}, Deadline: {task[3]}, Priority: {task[4]}, Status: {task[5]}")
        
        # Prompt for new details
        new_task_name = input(f"Enter new task name (or press Enter to keep the same): ") or task[1]
        new_subject = input(f"Enter new subject (or press Enter to keep the same): ") or task[2]
        new_deadline = input(f"Enter new deadline (YYYY-MM-DD) or press Enter to keep the same): ") or task[3]
        
        # Validating priority input
        valid_priorities = ['High', 'Medium', 'Low']
        new_priority = input(f"Enter new priority (High, Medium, Low or press Enter to keep the same): ") or task[4]
        while new_priority not in valid_priorities:
            print(f"Invalid priority. Please enter one of the following: {', '.join(valid_priorities)}")
            new_priority = input("Enter new priority (High, Medium, Low): ")
            
        # Updating the task in the database
        query = """
        UPDATE tasks 
        SET task_name = %s, subject = %s, deadline = %s, priority = %s
        WHERE task_id = %s AND user_id = %s"""
        cursor.execute(query, (new_task_name, new_subject, new_deadline, new_priority, task_id, user_id))
        conn.commit()
        
        print("Task updated successfully!")
    else:
        print("Task ID not found or does not belong to you.")
        
    cursor.close()
    conn.close()

# Progress report function
def progress_report(user_id):
    conn = connect_db()
    cursor = conn.cursor()
    
    # Fetch all tasks for the logged-in user
    query = "SELECT status FROM tasks WHERE user_id = %s"
    cursor.execute(query, (user_id,))
    tasks = cursor.fetchall()
    
    total_tasks = len(tasks)
    completed_tasks = sum(1 for task in tasks if task[0] == 'Completed')
    pending_tasks = total_tasks - completed_tasks
    
    # Displaying the progress summary
    print(f"\nProgress Report:")
    print(f"Total Tasks: {total_tasks}")
    print(f"Completed Tasks: {completed_tasks}")
    print(f"Pending Tasks: {pending_tasks}")
    
    # Calculating the completion percentage
    if total_tasks > 0:
        completion_percentage = (completed_tasks / total_tasks) * 100
        print(f"Completion Percentage: {completion_percentage:.2f}%")
    else:
        print("No tasks found.")
        
    cursor.close()
    conn.close()


def main():
    print("Welcome to the Study Planner!")
    
    while True:
        print("\n1. Create user")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            create_user()
        elif choice == "2":
            user_id = login()
            if user_id:
                while True:
                    print("\n1. Add a task")
                    print("2. View tasks")
                    print("3. Mark task as completed")
                    print("4. Show reminders")
                    print("5. Delete task")
                    print("6. Edit task")
                    print("7. Progress report")
                    print("8. Logout")
                    
                    sub_choice = input("Enter your choice: ")
                    
                    if sub_choice == "1":
                        add_task(user_id)
                    elif sub_choice == "2":
                        view_tasks(user_id)
                    elif sub_choice == "3":
                        mark_completed(user_id)
                    elif sub_choice == "4":
                        show_reminders(user_id)
                    elif sub_choice == "5":
                        delete_task(user_id)
                    elif sub_choice == "6":
                        edit_task(user_id)
                    elif sub_choice == "7":
                        progress_report(user_id)
                    elif sub_choice == "8":
                        break
                    else:
                        print("Invalid choice. Try again.")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()