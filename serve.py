from celery import Celery

app = Celery('celery', 
broker='amqp://guest:guest@localhost/guest_vhost',
backend='amqp://',
include=['tasks'])

