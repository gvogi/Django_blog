# django_blog

This Project was created as part of my Aueb Coding factory full stack developer bootcamp training.

Django blog is what its name implies.

A full featured Blog web app, made entirely by using Django Framework and Python.

Implements:

• Python (v3.11.3)

• Django (v4.2.2)

• SQLite3 

• Bootstrap5

• HTML5

• CSS3

The website uses Django's auth system for authentication and permission purposes.
Users can register (a profile is automatically created for them), log in, log out and ask for password reset via email.

Visitors have only read rights, while registered users can write new posts, and update or delete their own posts.
All users and visitors can use the navbar search, to find posts by title.

Users with staff status can additionally create announcements in the announcements board and edit or delete anything in the site, except from superusers posts or announcements.
Only superuser can delete what he has created and has the permission to edit or delete everything posted, by all the other users.

***** if project has data and you want to start clean, read "Clean projects data" instructions *****

How to run the project
In Windows OS: 
1. Open a new terminal in your vs code or any other code editor
2. To run the project create a venv in your root folder where your project is, with command:  
python -m venv venv
3. Activate the venv with:
venv\Scripts\activate
4. Navigate to your app folder with command: 
cd my_app_name   (ex: cd django_blog)
5. Import necessary packages from requirments.txt file with: 
pip install -r requirements.txt
If you notice that requirments where installed but intepreter gives you not imported modules notices, try to select intepreter manually by going to command pallete: ctrl+shift+p(vs code shortcut)→  Python: select interpreter→  and select the venv choice, usually is the recommended one by default.
6. Create a .env file in the root directory (directory where manage.py file is) and make the necessary changes to the file and to settings.py file.
A dummy .env file, of the original file used in this project is provided in the app, as a guide.
7. Make the necessary migrations with command: 
python manage.py makemigrations
8. And then commit with: 
python manage.py migrate
9. Create a superuser with: 
python manage.py createsuperuser
and follow the instructions in the terminal.
10. Register users you create
11. Create posts for these users (If you don’t want to do it manually check "How to Insert Posts" section below)
12. Test the functionality of the website


Clean projects data instructions
1. Delete venv file
2. Delete db, in windows command is:
del my_db_name (In our case: del db.sqlite3)
3. Delete all except, __pycache__  and  __init__.py, from migrations folders in blog and users app folders.
4. Delete .env file
5. Start from step 2 of "How to run the project" section of this doc.


How to Insert Posts:

To populate the site with some posts instead of writing them one by one, you can use the posts.json file included in resources file.
Put the file in the root directory (directory where manage.py file is).

** Attention, Before starting, create at least 2 users **

To use the file open a python shell in the terminal by typing:
1. python manage.py shell

Insert the following into the shell:
1. import json
2. from blog.models import Post
3. with open('posts.json') as f:
4.   posts_json = json.load(f)
5. for post in posts_json:
6.   post = Post(title=post['title'], content=post['content'], author_id=post['user_id'])
7. post.save()
8. If everything is alright exit the shell with:
exit()

If no errors occurred, your site now has posts and you are good to go.


Reset password via email:
Tested using Mailtrap’s email sandbox smtp.
1. Create a Mailtrap account with your email address.
2. After log in, from home page left side, click Email Testing and in Inboxes page, click your inbox name
3. In the right hand side, click into the bar underneath the Integrations label and
from the option menu, choose Django, from the options with title Python. 
4. Copy the snippet and paste it in the .env file or if not using one at the bottom of your settings.py file, in the project root folder.
Best way to copy the snippet is by using the copy to clipboard sign of the snippet itself.
5. If you didn’t use the copy to clipboard sign of the snippet and you don’t see the full credentials, to replace the ********* part of the EMAIL_HOST_PASSWORD of the snippet, click show credentials drop down menu, positioned above Integrations label and copy what you need and you are ready.
6. To test functionality go to the reset password page in our project (Forgot Password prompt in the login page) and ask for a reset password email.
In order for this to work you have to give the same mail you used for your mailtrap account, to one of your users and test the password reset on him.
7. After you give the email in the password reset form, you have to paste the http link from your mailtrap inbox, into the browsers address bar and reset your password in the next form.
8. Test by logging in (as the user who has the mailtrap email as his account email) with the new credentials. 
9. If you get error: SMTPServerDisconnected Exception Value: Connection unexpectedly closed , change the port of the Mailtrap smtp server in your .env file or settings.py.
Mailtrap provides 4 options, check the credentials drop down menu.
10. I you don’t find this way practical, according to Django docs, you can use the console email backend. This backend redirects all email to stdout allowing you to inspect the content of mail. 
