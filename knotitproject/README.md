Clone down repo and cd into it

Create virtual environment in Terminal:

python -m venv knotitenv
source ./knotitenv/bin/activate
Or create your Windows virtual environment in Command Line:

python -m venv knotitenv
source ./knotitenv/Scripts/activate
Install the app's dependencies:

pip install pillow
pip install django-embed-video
pip install -r requirements.txt
Build your database from the existing models:

python manage.py makemigrations knotitapp
python manage.py migrate
Create a superuser for your local version of the app:

python manage.py createsuperuser

python manage.py runserver

visit http://localhost:8000/