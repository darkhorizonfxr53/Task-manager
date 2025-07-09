# Task Manager Web Application

This project is a simple, yet fully functional web-based Task Manager application built using Python, Flask, JavaScript, and SQLite. It demonstrates a complete full-stack web app workflow including user authentication, task management, and data persistence.

---

## Overview

The Task Manager allows users to create personal task lists by registering or logging in with a unique username. Once logged in, users can add new tasks, view all their existing tasks, and delete tasks they no longer need. The app stores all data in a lightweight SQLite database, ensuring user tasks are saved between sessions.

This project is ideal for beginners looking to understand how frontend and backend technologies integrate to create interactive web applications. It also serves as a foundation to build upon with more advanced features such as password authentication, AJAX-based UI improvements, and more robust data handling.

---

## Technologies Used

- **Backend Framework:** [Flask](https://flask.palletsprojects.com/) — a lightweight and easy-to-use Python web framework.
- **Frontend:** HTML5, CSS3, and JavaScript for the user interface and client-side behavior.
- **Styling:** [Bootstrap 5](https://getbootstrap.com/) for responsive, mobile-friendly UI components and layout.
- **Database:** SQLite, a lightweight relational database stored in a single file (`tasks.db`), accessed through Python’s built-in `sqlite3` module.
- **Templating Engine:** Jinja2 (comes with Flask) for dynamic HTML rendering.

---

## Features

- **User Authentication:**
  Users can register or log in simply by entering a unique username. This session-based login tracks users and ensures task privacy.

- **Task Management:**
  Logged-in users can add new tasks via a simple form, view their current task list, and delete tasks individually.

- **Data Persistence:**
  All users and tasks are stored in a persistent SQLite database, ensuring that data remains intact between server restarts.

- **Responsive UI:**
  The app uses Bootstrap 5 to provide a clean and responsive design that works well on desktops, tablets, and mobile devices.

- **Client-Side Confirmation:**
  JavaScript is used to confirm task deletion to prevent accidental removals.

---

## Project Structure

task_manager/
├── app.py # Main Flask application with routes and logic
├── schema.sql # SQL schema file to create database tables
├── tasks.db # SQLite database file (created after setup)
├── requirements.txt # Python dependencies
├── static/
│ └── script.js # Client-side JavaScript (confirmation dialog)
├── templates/
│ ├── index.html # Main task management page template
│ └── login.html # User login page template
└── README.md # This documentation file

# YOUR PROJECT TITLE: TASK MANAGER
#### Video Demo:  <[URL HERE](https://youtu.be/dhfSNpXcEIA)>
#### Description:    This is a simple web-based Task Manager built using **Python (Flask)**, **JavaScript**, and **SQLite**. It allows users to register/login, add tasks, view them, and delete them.



