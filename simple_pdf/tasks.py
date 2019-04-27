import redis
import environ
# import os
import shutil
# from django.utils import timezone
# from django_rq import job
# import django_rq

env = environ.Env(
    DEBUG=(bool, False)
)
environ.Env.read_env('.env')

r = redis.Redis(host='localhost', port=env('PORT'), db=4)

def delete_later_pdf(uuid_remove):
    shutil.rmtree('pdfs/' + str(uuid_remove))
    return ('pdf ' + str(uuid_remove) + ' delete')
