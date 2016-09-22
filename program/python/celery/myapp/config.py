from __future__ import absolute_import
from kombu import Queue,Exchange
from datetime import timedelta

CELERY_TASK_RESULT_EXPIRES=3600
CELERY_TASK_SERIALIZER='json'
CELERY_ACCEPT_CONTENT=['json']
CELERY_RESULT_SERIALIZER='json'

CELERY_DEFAULT_EXCHANGE = 'agent'
CELERY_DEFAULT_EXCHANGE_TYPE = 'direct'

CELERT_QUEUES =  (
  Queue('machine1',exchange='agent',routing_key='machine1'),
  Queue('machine2',exchange='agent',routing_key='machine2'),
)
