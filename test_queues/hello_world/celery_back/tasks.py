from celery import Celery

from hello_world.celery_back import celeryconfig

celery_app = Celery('tasks')
celery_app.config_from_object(celeryconfig)


@celery_app.task()
def task_hello_world():
    print('Hello World (printed from tasks.py)')
    return 'Hello world (returned from tasks.py -> task_hello_world)'
