# Django-with-encrypted-database

## Installing dependencies

pip3 and python3 are required to run this application.

First install django:

`pip install django`

Then install cryptography

`pip install cryptography`

Note : It is recommended that you use a python virtual environment to keep the environment clean.

## Running this Django project

To run this project, cd into the main folder

`cd django_db_sec`

And run the runserver command

`python manage.py runserver`

The server will start executing on localhost:8000.

## Seeing the results

There are 3 pages which can be used to see the results of the project

### Data entry/Submit page

This page is on: 

`127.0.0.1:8000/`

This page is used to enter the name of the user. This new name will be encrypted and stored in the database. 

### Display page

This page is on 

`127.0.0.1:8000/display/`

This page shows all the encrypted and the corresponding decrypted versions of all the submitted users. ID is also added to be able to accurately correspond with the right pair.

### Admin page

This page is on 

`127.0.0.1:8000/admin/`

Use the following credentials to login into the admin page of Django

```
Username : user
Password : user
```

Once you have logon to this page, access the database by clicking on the Persons database. Here all the encrypted versions of the submitted names will be displayed. The corresponding ID will also be displayed which can be used to cross-check with the one on the Display page.

---
