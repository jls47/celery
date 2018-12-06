from celery import Celery
from holam import *
from serve import app



@app.task
def pscrape(args):
	scraper = portScrape(args[0], args[1], args[2])
	scraper.visit()

@app.task
def exscrape(args):
	scraper = exScrape(args[0], args[1], args[2])
	scraper.visit()
