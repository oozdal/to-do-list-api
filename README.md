# Todo List FastAPI Project

This project is a Todo List application built using FastAPI and SQLAlchemy. The goal of this project is to improve my FastAPI and fullstack development skills by following a Udemy FastAPI course: https://www.udemy.com/course/fastapi-the-complete-course/?couponCode=KEEPLEARNING

## Introduction

This project is part of my journey with FastAPI, a modern, fast (high-performance), web framework for building APIs with Python. It includes basic CRUD operations (Create, Read, Update, Delete) for managing Todo items.

## Features

- Create, Read, Update, and Delete Todo items.
- RESTful API endpoints for interacting with Todo items.
- Database integration for persistent storage.
- Authentication and authorization.

## Usage & Deployment

To-Do List App is deployed and accessible at: [Render](https://to-do-list-api-0o37.onrender.com/auth/) and [Railway](https://to-do-list-api-production-29ce.up.railway.app)

Warning: Free Instance Spin-Down Delay

Please note that the free instance provided by Render may experience spin-down due to inactivity. This could result in delays of 50 seconds or more when processing requests. Please be patient while your web browser tries to load the page.

![Screenshot 2024-04-21 at 12 29 10 PM](https://github.com/oozdal/to-do-list-api/assets/34719109/eafbfe2d-ab6c-4468-8f11-d9ea6846ee99)

![Screenshot 2024-04-21 at 12 35 42 PM](https://github.com/oozdal/to-do-list-api/assets/34719109/c0477ea8-67a2-4909-87bf-47fa9287b75d)

## Installation & Contribution

To run this project locally, follow these steps:

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/your-username/todo-list-fastapi.git

2. Navigate to the project directory:
   ```bash
   cd todo-list-fastapi/TodoApp2
   ```
3. Install the required dependencies:
  ```bash
  pip install -r requirements.txt
  ```

4. Run the FastAPI application:
   ```bash
   uvicorn main:app --reload
   ``` 

5. Access the application in your web browser at http://localhost:8000.

## Production Database

I rely on ElephantSQL, powered by PostgreSQL. Within my database schema, I maintain essential tables for managing user data and task information. 
Primarily, I focus on two pivotal tables: `users` and `todos`.

To gain a visual understanding of our TodoList application's inner workings, let's delve into some of its core members. Below, you'll find a snapshot showcasing the essence of my TodoList App:
Let's take a look at the users.

![Screenshot 2024-04-21 at 11 57 24 AM](https://github.com/oozdal/to-do-list-api/assets/34719109/006de07c-a1b1-4fbf-9be7-bfdf57903627)

One of the cornerstone elements of my application is the `todos` table, where all task-related data is meticulously organized and stored. Here's an overview of the structure and contents of our todos table:

![Screenshot 2024-04-21 at 12 02 05 PM](https://github.com/oozdal/to-do-list-api/assets/34719109/69d65e79-3d6e-4e8d-a38a-b6bbe3a00cf2)

In the app, each todo is intricately linked to its respective owner, as denoted by the `owner_id` field in the `todos` table. Let's visualize this relationship by joining the `users` and `todos` tables, showcasing all relevant rows where `user.id` matches `todos.owner_id`:

![Screenshot 2024-04-21 at 12 03 50 PM](https://github.com/oozdal/to-do-list-api/assets/34719109/9787a69f-86fa-466d-819c-a139c9ab61a3)

