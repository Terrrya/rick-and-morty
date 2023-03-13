# rick-and-morty


# How to RUN
- Created venv: `python -m venv ven`
- Activate it: `source venv/bin/activate`
- Install requirements: `pip install -r requirements.txt`
- Run migrations: `python manage.py migrate`
- Run Redis server: `docker run -d -p 6379:6379 redis`
- Run celery for task scheduling: `celery -A rick_and_morty_api worker -l INFO`
- Run celery beat for task scheduling: `celery -A rick_and_morty_api beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler   
`
- Create schedule for running sync in DB
- run app: `python manage.py runserver`