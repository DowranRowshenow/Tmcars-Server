from .base import *

DEBUG = True

ALLOWED_HOSTS = ["*"]

SECRET_KEY = "django-insecure-l+k$%nw4oi()n+1dxm*2uzuusj4hb1*%pu#qr-je95w47jz_$7"

INSTALLED_APPS += [
    "drf_spectacular",
]

SPECTACULAR_SETTINGS = {
    "TITLE": "Tmcars Project",
    "DESCRIPTION": "Tmcars REST API for mobile app.",
    "VERSION": "1.0.0",
    # "SERVE_INCLUDE_SCHEMA": False,
}
