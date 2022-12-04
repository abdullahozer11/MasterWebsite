testcommerce:
	@echo "testing commerce_app"
	coverage run manage.py test commerce_app/tests

testtodo:
	@echo "testing todo_app"
	coverage run manage.py test todo_app/tests

testportfolio:
	@echo "testing portfolio"
	coverage run manage.py test portfolio

test:
	@echo "testing all apps"
	coverage run manage.py test commerce_app/tests
	coverage run manage.py test todo_app/tests
	coverage run manage.py test portfolio

mm:
	@echo "makemigrations for all apps"
	python manage.py makemigrations commerce_app
	python manage.py makemigrations todo_app
	python manage.py makemigrations portfolio

m:
	@echo "migrate"
	python manage.py migrate

lint:
	pylint *
