from django.db import models
import logging
from django.core.signals import got_request_exception

def log(*args, **kwargs):
	logging.exception('error')

got_request_exception.connect(log)