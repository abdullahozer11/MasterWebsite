testcommerce:
	@echo "testing commerce_app"
	coverage run manage.py test commerce_app/tests

testtodo:
	@echo "testing todo_app"
	coverage run manage.py test todo_app/tests

test:
	@echo "testing all apps"
	coverage run manage.py test commerce_app/tests
	coverage run manage.py test todo_app/tests

mm:
	@echo "makemigrations for all apps"
	python manage.py makemigrations commerce_app
	python manage.py makemigrations todo_app

m:
	@echo "migrate"
	python manage.py migrate

lint:
	pylint *
