from time import sleep
from django.conf import settings
from celery import Celery


BROKER_URL = 'amqp://songxr:IloveU@localhost:5672/vhost'

class MyRouter(object):
    def route_for_task(self, task, args=None, kwargs=None):
        print("ROUTE FOR TASK: %r" % (task, ))
        if task.startswith('my_tasks'):
            return {
                "exchange": "default_songxr",
                "exchange_type": "direct",
                "routing_key": "default_songxr"
            }
        if task.startswith('topictest'):
            return {
                'queue': 'topicqueue',
            }
        elif task.startswith('dongwm.tasks.test'):
            return {
                "exchange": "broadcast_tasks",
            }
        else:
            return None
CELERY_ROUTES = (MyRouter(), )

app = Celery('tasks', backend = 'db+mysql://django:djtest@localhost/django', broker=BROKER_URL)
app.conf.update(
    CELERY_ROUTES = (MyRouter(), ),
    #CELERY_ROUTES = { 'dashbaord.tasks.add': {'queue': 'default_songxr'}, },
    )

@app.task
def add(x, y):
    sleep(5)
    return x + y
