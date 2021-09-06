# broker responsible for delivering messages to celery
broker_url = 'redis://localhost:6379/0'
# if you want to read task's state, result
result_backend = 'redis://localhost'
# enable task state reporting
task_track_started = True
# number of worker processes
worker_concurrency = 5
