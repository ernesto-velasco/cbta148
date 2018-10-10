# CBTA148
Web project for a school to accredit social service.
## Builded With
* htm
* css
* Python 3.7
* [Django](https://www.djangoproject.com/) - Python Web framework
* [Materialize](https://materializecss.com/) - css framework


## Installing
### Clone or download the proyect
```
Git clone https://github.com/vegonz/cbta148.git
```
### Create a virtual enviorement
```
cd cbta148
```
```
python -m venv myvenv
```
```
myvenv\Scripts\activate
```
### Install Django
```
pip instal django==2.1
```
## Configuration
```
cd cbtaSite
```
Forms models is using an ImageField so installing Pillow is required
```
pip install pillow
```

```
python manage.py migrate
```
Create a super user, it will ask to add a username, an email and a password
```
python manage.py createsuperuser
```
Now we can run the project
```
python manage.py runserver
```
For now only an empty page will appear
```
localhost:8000
```
To add content enter this link with the super user credentials and add content to the db

```
localhost:8000/admin
```

See it in action on a test host
http://cbta148.pythonanywhere.com/

## Authors
* [Velasco González Ernesto](https://github.com/vegonz/)
* Reyes Reyes Vanessa
* Rios Mancilla Christian
