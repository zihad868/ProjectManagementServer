## Django  Project Management API

#  API Documentation 
-  http://127.0.0.1:8000/api-listing/
-  http://127.0.0.1:8000/api-documentation/

  
  ## Features
- User Management: Register, log in, retrieve, update, and delete user accounts.
- Project Management: Create, list, update, and delete projects with owner and member roles.
- Task Management: CRUD operations on tasks within projects with priority and status tracking.
- Comment Management: Commenting on tasks with retrieval, updates, and deletions.

  ##  Authentication
- After logging in, include the token in the Authorization header:
  Authorization:  Bearer access token


## Clone and Run Local Manually 
-  pip install virtualenv 
-  virtualenv env                    --->  ( For Linux )
-  source ./env/bin/activate   --->  ( For Linux )
-  pip install django
-  pip install djangorestframework
-  pip install djangorestframework-simplejwt
-  pip install drf-yasg
-  git clone https://github.com/zihad868/ProjectManagementServer.git
-  cd ProjectManagementServer
-  python manage.py makemigrations
-  python manage.py migrate 
-  python manage.py runserver

## OR Git Clone & go to main project directory run
 -  pip install -r requirements.txt
 -  cd ProjectManagementServer
 -  python manage.py makemigrations
 -  python manage.py migrate 
 -  python manage.py runserver


  
Users
Register User (POST /api/users/register/): Create a new user.
Login User (POST /api/users/login/): Authenticate a user and return a token.
Get User Details (GET /api/users/{id}/): Retrieve details of a specific user.
Update User (PUT/PATCH /api/users/{id}/): Update user details.
Delete User (DELETE /api/users/{id}/): Delete a user account.
- Projects
List Projects (GET /api/projects/): Retrieve a list of all projects.
Create Project (POST /api/projects/): Create a new project.
Retrieve Project (GET /api/projects/{id}/): Retrieve details of a specific
project.
Update Project (PUT/PATCH /api/projects/{id}/): Update project details.
Delete Project (DELETE /api/projects/{id}/): Delete a project.
- Task
List Tasks (GET /api/projects/{project_id}/tasks/): Retrieve a list of all tasks in
a project.
Create Task (POST /api/projects/{project_id}/tasks/): Create a new task in a
project.
Retrieve Task (GET /api/tasks/{id}/): Retrieve details of a specific task.
Update Task (PUT/PATCH /api/tasks/{id}/): Update task details.
Delete Task (DELETE /api/tasks/{id}/): Delete a task.
