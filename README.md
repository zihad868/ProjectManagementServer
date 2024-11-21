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
-  python manage.py createsuperuser
-  python manage.py runserver

## OR Git Clone & go to main project directory run
 -  pip install -r requirements.txt
 -  cd ProjectManagementServer
 -  python manage.py makemigrations
 -  python manage.py migrate 
 -  python manage.py runserver


API Endpoints
Users
Method	Endpoint	Description
POST	/api/users/register/	Register a new user.
POST	/api/users/login/	Authenticate a user.
GET	/api/users/{id}/	Retrieve user details.
PUT	/api/users/{id}/	Update user details.
DELETE	/api/users/{id}/	Delete a user account.
Projects
Method	Endpoint	Description
GET	/api/projects/	List all projects.
POST	/api/projects/	Create a new project.
GET	/api/projects/{id}/	Retrieve project details.
PUT	/api/projects/{id}/	Update a project.
DELETE	/api/projects/{id}/	Delete a project.
Tasks
Method	Endpoint	Description
GET	/api/projects/{project_id}/tasks/	List all tasks in a project.
POST	/api/projects/{project_id}/tasks/	Create a new task.
GET	/api/tasks/{id}/	Retrieve task details.
PUT	/api/tasks/{id}/	Update a task.
DELETE	/api/tasks/{id}/	Delete a task.
Comments
Method	Endpoint	Description
GET	/api/tasks/{task_id}/comments/	List all comments on a task.
POST	/api/tasks/{task_id}/comments/	Add a comment to a task.
GET	/api/comments/{id}/	Retrieve a specific comment.
PUT	/api/comments/{id}/	Update a comment.
DELETE	/api/comments/{id}/	Delete a comment.
