all: django git
	django-admin startproject mysite

django:
	sudo dnf -y install python3-django
git:
	sudo dnf -y install git
runsite:
	python3 mysite/manage.py runserver
