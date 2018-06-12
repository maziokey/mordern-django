from .base import *


SECRET_KEY = env('DJANGO_SECRET_KEY', default='(fuk6t4kzluxz57d2&6*zc*a2j*=gqc%uo(su#koe-^!orzl#j')


DEBUG = env.bool('DJANGO_DEBUG', default=True)
