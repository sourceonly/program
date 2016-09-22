from __future__ import absolute_import
from celery import Celery
app = Celery('myapp',
             broker='amqp://guest@192.168.0.90//',
             backend='amqp://guest@192.168.0.90//',
             include=['myapp.agent'])

app.config_from_object('myapp.config')

if __name__ == '__main__':
  app.start()
