from .base import *

DEBUG = False

ALLOWED_HOSTS = ["dowranrowshenow.pythonanywhere.com"]

INSTALLED_APPS += [
    "cloudinary_storage",
    "cloudinary",
]

DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"
