.PHONY: run pre-staging

pre-staging:
	pip install -r requirements.txt
	export FLASK_APP='./APIs/app.py'

run:
	flask run -p 5002 &
	sleep 2
	python3 ./pre-checks.py
	python3 ./main.py
