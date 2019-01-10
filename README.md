# CBTA148
Web project for a school to accredit social service.
## Built With
* html
* css
* [Python 3.7](https://www.python.org/)
* [Django 2.1](https://www.djangoproject.com/) - Python Web framework
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

## Authors
* [Velasco González Ernesto](https://github.com/vegonz/)
* Reyes Reyes Vanessa
* [Rios Mancilla Christian](https://github.com/chris182xD)
