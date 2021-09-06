from flask import Flask

from hello_world.celery_back import tasks

app = Flask(__name__)


@app.route('/hello', methods=['GET', 'POST'])
def hello():
    tasks.task_hello_world.apply_async()
    return 'hello (returned from vanguard.py -> hello)'
