Project Description: To-Do List Management System

Objective:
Develop a web application using Django and Django REST Framework to manage a To-Do List.

Key Components:
1. Data Models:
   - Task: Represents an individual task in the list.
     Fields: title (task title), description (task description), done (completion status).

2. API:
   - CRUD Operations: API endpoints for creating, reading, updating, and deleting tasks.
   - Custom Action: API endpoint for marking a task as "done".

3. Serialization:
   - Converts Task model data into JSON format for API communication.

4. Testing:
   - Automated tests to verify API functionality:
     - Create, read, update, and delete tasks.
     - Mark tasks as "done".

5. Project Setup:
   - Dependency management using pipenv.
   - SQLite database configuration for storing tasks (for simplicity).
   - URL routing setup using DefaultRouter in Django REST Framework.

6. Installed Packages:
   - Django: Core web framework for Python.
   - Django REST Framework: Extension for creating APIs in Django.
   - pytest, pytest-django: Used for writing and running tests.
   - Additional packages as per project requirements.

Future Plans:
- Implement user authentication and authorization (optional).
- Integrate a frontend interface for user-friendly interaction with the To-Do List.
- Enhance UI/UX design for improved user experience.
- Deploy the project to a server for public use (optional).
