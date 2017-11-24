from .base import base.py local.py production.py test.py

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('DJANGO_SECRET_KEY', default='_wu1qzq4g!dzr0t%xeanbnx3kjo%khi^dr@86gg2-rq=7c)nxr')