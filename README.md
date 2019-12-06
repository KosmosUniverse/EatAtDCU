# Eat@DCU

Eat@DCU is a web application for DCU restaurants.

## Download

```bash
git clone git@gitlab.computing.dcu.ie:ducrett2/2020-ca377-ducrett2-eatatdcu.git
```

## Requirements

You will need python 3.6 and Django for this project.


## Usage

You can launch the server with this command:

```bash
python3 manage.py runserver
```

After that, open a web browser and enter in the url bar:
```
localhost:8000/eatatdcu
```
Or,
```
http://127.0.0.1:8000/eatatdcu
```

## Deploy

To deploy you need a [pythonanywhere]https://www.pythonanywhere.com account.

1. Go in "Console" tab and create a new console
2. Make a new virtualenv
```bash
$ mkvirtualenv --python=/usr/bin/python3.6 ca377-virtualenv
(ca377-virtualenv)$ pip install django==2.2.4
(ca377-virtualenv)$ pip install requests
```
4. Clone your repository
```bash
git clone https://<path to your repo>
```
5. From the "Web" tab create a new web app with manual configuration and python 3.6.
6. Edit your web app paths with the path to your src directory
7. Edit WSCI configuration file, remove verything except DJango part and set the path ans the os.environ['DJANGO_SETTING_MODULE'].
8. In "File" tab, edit settings.py file by adding 'YOUR_ACCOUNT_NAME.pythonanywhere.com' to the list of ALLOWED_HOSTS.
9. Setup your database:
```bash
(mysite-virtualenv) $ python manage.py makemigrations eatatdcu
(mysite-virtualenv) $ python manage.py migrate 
(mysite-virtualenv) $ python manage.py shell >>>import load_db_data
```
11. Now you can access to your web app with a link like 'YOUR_ACCOUNT_NAME.pythonanywhere.com/eatatdcu'.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Credits

2020-ca377-master-eatatdcu

Master repository for Fundamentals of Programming III (CA377)
