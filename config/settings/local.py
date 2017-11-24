from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('DJANGO_SECRET_KEY', default='_wu1qzq4g!dzr0t%xeanbnx3kjo%khi^dr@86gg2-rq=7c)nxr')

# SECURITY WARNING: don't run with debug turned on in production!
# We should always assume that DEBUG will be False, except in local development where it is True
DEBUG = env.bool('DJANGO_DEBUG', default=True)
