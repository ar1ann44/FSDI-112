# Steps to create a Django project
 
1. Create the folder of the project

2. Open a terminal at that folder

3. Create the virtual environment
 
    - Mac: python3 -m venv venv
    - Windows: python/py -m venv venv
 
4. Activate the virtual environment
 
    - Mac: source venv/bin/activate
    - Windows: .\venv\Scripts\activate
 
5. Install the required dependencies
 
    - Both OS: pip3 install django
 
### Extra
 
    - **touch** : this command allow us to create a file from the Mac OS terminal (touch FILENAME.EXTENSION)
    - **mkdir** : this is for creating a folder


6. Create the django project structure
 
    - Both OS: django-admin startproject NAME_FOLDER .


7. Create a django app:
    both OS: python3 manage.py startapp NAME_OF_THE_APP

## Models in Django

Our models needs to be written inside of the models.py file on any application.
When we finish them we need to run these commands:

    1. "python3 manage.py makemigrations" - Django will create a migration interpreting the new model
    2. "python3 manage.py migrate" - Django will apply the created migration file to the database