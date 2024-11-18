## Django  Project Management API
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


## Clone and Run Local
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

  
